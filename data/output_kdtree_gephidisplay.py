import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import time
# import psutil
import laspy

# Read the LAS file and convert it into a point cloud

las_file = laspy.read("Tree/tree_chunked_distance=2.las")

point_cloud = np.vstack((las_file.x, las_file.y, las_file.z)).transpose()

# k-d Tree Data Structure
class Node:
    def __init__(self, points, depth=0, max_depth=5, max_points=8):
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

# Export viaulization for Gephi
pos = nx.spring_layout(graph, k=0.2)

degrees = dict(nx.degree(graph))

nx.draw(graph, pos=pos, nodelist=degrees.keys())

# plt.show()

# Write to Gephi

nx.write_gexf(graph, "gephis/tree/tree_chunked_distance=2_kdtree.gexf")

