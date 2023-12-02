import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import time
import laspy

# Read the LAS file and convert it into a point cloud
las_file = laspy.read("StreetLight_FlyOver.las")
#las_file = laspy.read("House_FlyOver.las")
#las_file = laspy.read("Tree_FlyOver.las")
las_points = np.vstack((las_file.x, las_file.y, las_file.z)).transpose()

# Timer starts after reading LAS file
start_time = time.time()

# Octree Data Structure
class Node:
    def __init__(self, points, center, half_width, depth=0, max_depth=5, max_points=8):
        self.points = points
        self.center = center
        self.half_width = half_width
        self.depth = depth
        self.children = []
        self.id = np.random.randint(1e4)  # assign unique identifier of each node

        if len(points) > max_points and depth < max_depth:
            self.subdivide()

    def subdivide(self):
        for dx in [-0.5, 0.5]:
            for dy in [-0.5, 0.5]:
                for dz in [-0.5, 0.5]:
                    new_center = [self.center[0] + dx * self.half_width,
                                  self.center[1] + dy * self.half_width,
                                  self.center[2] + dz * self.half_width]
                    child_points = [pt for pt in self.points if self.point_found(pt, new_center)]
                    if len(child_points) > 0:
                        child = Node(child_points, new_center, self.half_width * 0.5, self.depth + 1)
                        self.children.append(child)

    def point_found(self, point, center):
        hw = self.half_width * 0.5
        return (center[0] - hw <= point[0] <= center[0] + hw and
                center[1] - hw <= point[1] <= center[1] + hw and
                center[2] - hw <= point[2] <= center[2] + hw)

# Create Octree with LAS file points
center = np.mean(las_points, axis=0)
half_width = np.max(np.ptp(las_points, axis=0) / 2.0)
root = Node(las_points, center, half_width)

# Visualize Octree structure of Point Cloud file
def octree_visualization(graph, root, root_id):
    for child in root.children:
        child_id = child.id
        graph.add_node(child_id)
        graph.add_edge(root_id, child_id)
        octree_visualization(graph, child, child_id)

graph = nx.Graph()
root_id = root.id
graph.add_node(root_id)
octree_visualization(graph, root, root_id)
degrees = dict(nx.degree(graph))

# Visualization
max_degree = max(degrees.values())
min_degree = min(degrees.values())
normalized_degrees = [(d - min_degree)/(max_degree - min_degree) for d in degrees.values()]
cmap = plt.get_cmap('coolwarm')
nx.draw(graph, pos=nx.spring_layout(graph),
        nodelist=degrees.keys(),
        node_size=[s * 50 for s in degrees.values()],
        node_color=[cmap(c) for c in normalized_degrees])

# Timer stops
end_time = time.time()

print('Performance: ', end_time - start_time, ' seconds\n')

plt.show()
