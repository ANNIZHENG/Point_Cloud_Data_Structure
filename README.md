## NYUVIP-Point-Cloud-Data-Structure
### NYU Urban LiDAR and Remote Sensing (GY) Team Project

#### Create a virtual environment to run the programs in tests directory
```
python3.9 -m venv ENV_NAME
source ENV_NAME/bin/activate
pip install open3d
pip install networkx
```

#### Sample point cloud data shape: (196133, 3)
<img src="images/sample_original.png" alt="The Original Sample File" width="300" height="200">

#### Analyze the Sample Point Cloud file in Octree Structure using Open3D
<img src="images/sample_3d_octree_depth=5.png" alt="3D Visualization of Octree with max depth = 5" width="300" height="300">
<img src="images/sample_3d_octree_depth=3.png" alt="3D Visualization of Octree with max depth = 3" width="300" height="300">

#### Analyze the Sample Point Cloud file in Octree Structure using Matplotlib, NetworkX, NumPy
<img src="images/sample_2d_octree_depth=5.png" alt="2D Visualization of Octree with max depth = 5" width="300" height="200">
<img src="images/sample_2d_octree_depth=3.png" alt="2D Visualization of Octree with max depth = 3" width="300" height="200">

#### A Better Visualization in 2D?
<img src="images/sample_2d_octree_depth=3_.png" alt="A Better 2D Visualization of Octree with max depth = 3" width="300" height="200">

#### Time spent of running tests/test2_networkx.py in relation to the desired depth of the Octree
Time Spent = Time to load data file + Time to Construct Octree + Time to Visualize data file
| Depth         | Time Spent(s) |
| ------------- |:-------------:|
| 3             | ~1.41         |
| 4             | ~1.97         |
| 5             | ~4.84         |