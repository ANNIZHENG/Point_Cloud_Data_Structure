import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Randomly generated point cloud
num_points = 1000
point_cloud = np.random.rand(num_points, 3) * 10 # number generated between [0, 10]

# Octree Structure
class Node:
    def __init__(self, points, depth=0):
        self.points = points
        self.children = []
        self.depth = depth
        self.id = np.random.randint(100000)
        
        if len(points) > 50 and depth < 3: 
            self.split()
        
    def split(self):
        median = np.median(self.points, axis=0)
        masks = [
            self.points[:, i] < median[i]
            for i in range(3)
        ]
        octants = [
            np.logical_and(masks[i], masks[j])
            for i in range(3)
            for j in range(3)
            if i != j
        ]
        
        for mask in octants:
            self.children.append(Node(self.points[mask], self.depth+1))

# Creating an Octree
root = Node(point_cloud)

# Visualization
def visualize_octree_and_vine(node, graph, prev_id=None):
    if prev_id:
        graph.add_edge(prev_id, node.id)
    
    plt.scatter(node.points[:, 0], node.points[:, 1], alpha=0.5, s=10)
    
    for child in node.children:
        visualize_octree_and_vine(child, graph, node.id)

plt.figure(figsize=(12, 6))

# plt.subplot(121)
# graph = nx.Graph()
# visualize_octree_and_vine(root, graph)
# plt.title("Octree Structure")

plt.subplot(122)
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=15)
plt.title("Vine-like Structure")

plt.tight_layout()
plt.show()








