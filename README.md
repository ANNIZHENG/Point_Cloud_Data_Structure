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
The Original Sample File

#### Analyze the Sample Point Cloud file in Octree Structure using Open3D
<img src="images/compare_test_3d.png" alt="Compare 3D Test Visualizations" width="550" height="250">

#### Analyze the Sample Point Cloud file in Octree Structure using Matplotlib, NetworkX, NumPy
<img src="images/compare_test_2d.png" alt="Compare 2D Test Visualizations" width="500" height="250">

#### A Better Visualization in 2D?
<img src="images/sample_2d_octree_depth=3_.png" alt="A Better 2D Visualization of Octree with max depth = 3" width="400" height="250">

#### Time spent of running tests/test2_networkx.py in relation to the desired depth of the Octree
Time Spent = Time to load data file + Time to Construct Octree + Time to Visualize data file
| Depth         | Time Spent(s) |
| ------------- |:-------------:|
| 3             | ~1.41         |
| 4             | ~1.97         |
| 5             | ~4.84         |