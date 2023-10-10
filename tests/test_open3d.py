import open3d as o3d
import numpy as np
# import time

ply_point_cloud = o3d.data.PLYPointCloud() # redwood living room dataset from the official website
pcd = o3d.io.read_point_cloud(ply_point_cloud.path)

## Octree Geometry 

# - suitable for representing sparce scenes where the distribution across varies
# - memory efficient
# - hierarchical way of organizing point cloud data; root node being the entire 3D space; when combining all octants (child nodes) together, the collectively represent the entire 3D space, each cube is a specific portion of the space
# - adaptive - data compression available


# start_time = time.time()

octree = o3d.geometry.Octree(max_depth=5)
octree.convert_from_point_cloud(pcd, size_expand=0.01)
o3d.visualization.draw_geometries([octree])

# octree_time = time.time() - start_time

# print(octree_time)

octree = o3d.geometry.Octree(max_depth=3)
octree.convert_from_point_cloud(pcd, size_expand=0.01)
o3d.visualization.draw_geometries([octree])

# print(octree_time)



## Simple numpy operations

# print(pcd) # PointCloud with 196133 points.
# print(np.asarray(pcd.points))

## Visualize point cloud data

# zoom - the smaller the number the closer it is to the data
# front - front vector of the camera
# lookat - lookat vector of the camera
# up - up vector of the camera

# pcd.paint_uniform_color([0.5, 0.5, 1]) # RGB
# o3d.visualization.draw_geometries([pcd],
# 									zoom=0.4,
# 									front=[0.4, -0.2, -0.8],
# 									lookat=[2.6, 2, 1.5],
# 									up=[-0.0694, -0.9768, 0.2024])


## Visualize point cloud data - hidden point removal

# diameter = np.linalg.norm(np.asarray(pcd.get_max_bound()) - np.asarray(pcd.get_min_bound())) # distance of the camera from the center of the scene of point cloud
# camera = [0, 0, diameter] # camera is located at the original coordinate system (0, 0, 0)
# radius = diameter * 100 #  points in the point cloud that are within this radius from thecamera's viewpoint are considered visible

# _, background = pcd.hidden_point_removal(camera, radius)

# pcd = pcd.select_by_index(background)
# o3d.visualization.draw_geometries([pcd])

## Voxel-grid Geometry

# - layers of 3D cube in space
# - memory intensive and inefficiency for sparce data
# - suitable for representing scenes with regular structures or where resolution is constant throughout space

# voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd, voxel_size=0.05)
# o3d.visualization.draw_geometries([voxel_grid],
# 									zoom=0.4,
# 									front=[0.4, -0.2, -0.8],
# 									lookat=[2.6, 2, 1.5],
# 									up=[-0.0694, -0.9768, 0.2024])


## Volxel downsample

# - memory efficient compared to vocel-grid approach and good to deal with sparce data
# - noise reduction (simplified version of the file) and vidualization

# voxel_grid_down = pcd.voxel_down_sample(voxel_size=0.05)
# o3d.visualization.draw_geometries([voxel_grid_down],
# 									zoom=0.4,
# 									front=[0.4, -0.2, -0.8],
# 									lookat=[2.6, 2, 1.5],
# 									up=[-0.0694, -0.9768, 0.2024])

