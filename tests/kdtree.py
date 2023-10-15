import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import open3d as o3d
import time

def visualize_kdtree(max_depth):
    start_time = time.time()

    # Retrieve an actual Point Cloud file
    point_cloud_file = o3d.io.read_point_cloud(o3d.data.PLYPointCloud().path)
    point_cloud = np.asarray(point_cloud_file.points)

    # KDTree Data Structure
    class Node:
        def __init__(self, points, depth=0, max_depth=max_depth):
            self.points = points
            self.axis = depth % 3
            self.left = None
            self.right = None
            self.id = np.random.randint(1e4)

            # Sort points by axis
            self.points = sorted(points, key=lambda point: point[self.axis])
            median = len(self.points) // 2
            self.median_point = self.points[median]

            # Split the set of points into two halves
            if depth < max_depth:
                if len(self.points[:median]) > 0:
                    self.left = Node(self.points[:median], depth + 1)
                if len(self.points[median + 1:]) > 0:
                    self.right = Node(self.points[median + 1:], depth + 1)

    # Create KDTree
    root = Node(point_cloud)

    # Visualize KDTree structure of Point Cloud file
    def kdtree_visualization(graph, node, parent_id):
        if node:
            current_id = node.id
            graph.add_node(current_id)
            if parent_id is not None:
                graph.add_edge(parent_id, current_id)
            kdtree_visualization(graph, node.left, current_id)
            kdtree_visualization(graph, node.right, current_id)

    graph = nx.Graph()
    kdtree_visualization(graph, root, None)
    degrees = dict(nx.degree(graph))

    # normalize degrees
    max_degree = max(degrees.values())
    min_degree = min(degrees.values())
    normalized_degrees = [(d - min_degree)/(max_degree - min_degree) for d in degrees.values()]

    cmap = plt.get_cmap('coolwarm')
    nx.draw(graph, pos=nx.spring_layout(graph),
            nodelist=degrees.keys(),
            node_size=[s * 50 for s in degrees.values()],
            node_color=[cmap(c) for c in normalized_degrees])

    end_time = time.time()

    print(f'Performance for max_depth {max_depth}: ', end_time - start_time, '\n')

    plt.title(f"KDTree with Maximum Depth = {max_depth}")
    plt.show()

# Call the function for different max_depth values
visualize_kdtree(3)
visualize_kdtree(5)
