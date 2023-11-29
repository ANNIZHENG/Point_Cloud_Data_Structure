import numpy as np
from scipy.spatial import KDTree
import time

#generate a large 3D point cloud
point_cloud = np.random.rand(1000000, 3)  # 1 million random 3D points

#building the k-d tree and measuring the time taken, which is indexing
start_time = time.time()
kd_tree = KDTree(point_cloud)  #building the k-d tree
kd_tree_build_time = time.time() - start_time
print(f"Time to build k-d tree: {kd_tree_build_time:.2f} seconds")

#nearest neighbor search
query_point = np.random.rand(1, 3)  #a random query point
start_time = time.time()
distance, index = kd_tree.query(query_point)  #this is nearest neighbor search
nn_search_time = time.time() - start_time
print(f"Time for nearest neighbor search: {nn_search_time:.6f} seconds")

#range search
radius = 0.05
start_time = time.time()
indices = kd_tree.query_ball_point(query_point, radius)  #this is range search
range_search_time = time.time() - start_time
print(f"Time for range search: {range_search_time:.6f} seconds")
