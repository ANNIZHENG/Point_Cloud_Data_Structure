
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import open3d as o3d

start_time = time.time() # Timer starts

# Retrieve an actual Point Cloud file
point_cloud_file = o3d.io.read_point_cloud(o3d.data.PLYPointCloud().path)
point_cloud = np.asarray(point_cloud_file.points) # shape: (196133, 3) - there are 195133 cooridnates of (x,y,z)

# Octree Data Structure
class Node:
    def __init__(self, points, center, half_width, depth=0, max_depth=3, max_points=8): # max_depth=6, max_points=8*8?
        self.points = points
        self.center = center
        self.half_width = half_width
        self.depth = depth # max depth to preven overfitting
        self.children = []
        self.id = np.random.randint(1e4)  # assign unique identifier of each node

        # Subdivide node into eight children if reach the bounding box
        if len(points) > max_points and depth < max_depth:
            self.subdivide()

    def subdivide(self): # Use bounding box to find child nodes
        for dx in [-0.5, 0.5]: # traverse through the x-axis of the point cloud coordinate
            for dy in [-0.5, 0.5]: # traverse through the y-axis
                for dz in [-0.5, 0.5]: # traverse through the z-axis

                    # Create new centroid for finding child node
                    new_center = [self.center[0] + dx * self.half_width,
                                self.center[1] + dy * self.half_width,
                                self.center[2] + dz * self.half_width]
                    
                    # Find points inside the boudning box
                    child_points = [pt for pt in self.points if self.point_found(pt, new_center)]
                    
                    # If there are points, create child node
                    if len(child_points) > 0:
                        child = Node(child_points, new_center, self.half_width*0.5, self.depth+1)
                        self.children.append(child)
                    
    def point_found(self, point, center):
        hw = self.half_width * 0.5  # new half width
        return (center[0] - hw <= point[0] <= center[0] + hw and 
                center[1] - hw <= point[1] <= center[1] + hw and
                center[2] - hw <= point[2] <= center[2] + hw)

# Create Octree
center = np.mean(point_cloud, axis=0) # Center of where the Octree starts subdeviding
half_width = np.max(np.ptp(point_cloud, axis=0)/2.0)
root = Node(point_cloud, center, half_width)

# Visualize Octree structure of Point Cloud file
def octree_visualization(graph, root, root_id):
    for child in root.children:
        # Create a unique identifier for the graph node
        child_id = child.id

        # Add a node to the graph
        graph.add_node(child_id)

        # Add an edge between the parent node and the child node
        graph.add_edge(root_id, child_id)

        # Recurse into child node
        octree_visualization(graph, child, child_id)

graph = nx.Graph()
root_id = root.id

# Add nodes and edges through traversing the octree
graph.add_node(root_id)
octree_visualization(graph, root, root_id)

end_time = time.time() # Timer stops

print('Performance: ', end_time - start_time, '\n')


# Export viaulization for Gephi
pos = nx.spring_layout(graph, k=0.2)

degrees = dict(nx.degree(graph))

nx.draw(graph, pos=pos, nodelist=degrees.keys())

plt.show()

nx.write_gexf(graph, 'test2_gephi_octree.gexf')



