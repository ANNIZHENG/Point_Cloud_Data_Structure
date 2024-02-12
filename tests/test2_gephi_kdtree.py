import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import open3d as o3d
import time
import psutil

start_time = time.time()  # Timer starts
initial_memory = psutil.Process().memory_info().rss / (1024 * 1024) # Memory check starts

# Retrieve an actual Point Cloud file
point_cloud_file = o3d.io.read_point_cloud(...) # las file path here
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
final_memory = psutil.Process().memory_info().rss / (1024 * 1024) #Memory check ends
memory_used = final_memory - initial_memory

print('Performance: ', end_time - start_time, '\n')
print('Memory Used: ', memory_used, 'MB')

nx.write_gexf(graph, ...) # output file name here

'''
Performance: 

House
K-D Tree Performance:  1.7642369270324707
K-D Tree Memory Used:  221.484375 MB

Tree
K-D Tree Performance:  1.0891039371490479
K-D Tree Memory Used:  143.546875 MB

Streetlight
K-D Tree Performance:  0.07814693450927734
K-D Tree Memory Used:  9.84375 MB
'''
