import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import open3d as o3d
import time

start_time = time.time()  # Timer starts

# Retrieve an actual Point Cloud file
point_cloud_file = o3d.io.read_point_cloud(o3d.data.PLYPointCloud().path)
point_cloud = np.asarray(point_cloud_file.points)  # Retrieve the points

# k-d Tree Data Structure
class Node:
    def __init__(self, points, depth=0, max_depth=10, max_points=8):
        self.points = points
        self.axis = depth % 3  # Choose axis based on depth
        self.depth = depth
        self.children = []
        self.id = np.random.randint(1e4)  # Assign unique identifier for each node

        if len(points) > max_points and depth < max_depth:
            self.split()

    def split(self):
        sorted_points = sorted(self.points, key=lambda point: point[self.axis])
        median_idx = len(sorted_points) // 2
        median_point = sorted_points[median_idx]

        left_points = sorted_points[:median_idx]
        right_points = sorted_points[median_idx+1:]

        if left_points:
            self.children.append(Node(left_points, self.depth+1))
        if right_points:
            self.children.append(Node(right_points, self.depth+1))

# Create k-d Tree
root = Node(point_cloud)

# Visualize k-d tree structure of Point Cloud
def kdtree_visualization(graph, node, node_id):
    for child in node.children:
        child_id = child.id
        graph.add_node(child_id)
        graph.add_edge(node_id, child_id)
        kdtree_visualization(graph, child, child_id)

graph = nx.Graph()
root_id = root.id

graph.add_node(root_id)
kdtree_visualization(graph, root, root_id)

end_time = time.time()  # Timer stops

print('Performance: ', end_time - start_time, '\n')


# Export viaulization for Gephi
pos = nx.spring_layout(graph, k=0.2)

degrees = dict(nx.degree(graph))

nx.draw(graph, pos=pos, nodelist=degrees.keys())

plt.show()

nx.write_gexf(graph, 'test2_gephi_kdtree.gexf')


