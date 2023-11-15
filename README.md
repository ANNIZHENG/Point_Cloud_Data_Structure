## NYUVIP-Point-Cloud-Data-Structure
### NYU Urban LiDAR and Remote Sensing (GY) Team Project

#### Create a virtual environment to run the programs in tests directory
```
python3.9 -m venv ENV_NAME
source ENV_NAME/bin/activate
pip install open3d
pip install networkx
```

#### Sample Point Cloud File
<img src="images/sample_data.png" width="300" height="200">

#### Analyze Sample Point Cloud File in Open3D
<img src="images/test0_octree.png" width="550" height="250">

#### Analyze Sample Point Cloud File in Octree Structure using Matplotlib, NetworkX, NumPy, and Gephi
<img src="images/test2_gephi_octree.png" width="300" height="300">

#### Analyze Sample Point Cloud File in K-D Tree Structure using Matplotlib, NetworkX, NumPy, and Gephi
<img src="images/test2_gephi_kdtree.png" width="300" height="300">

<!-- #### Time spent of running tests/test2_networkx.py in relation to the desired depth of the Octree
Time Spent = Time to load data file + Time to Construct Octree + Time to Visualize data file
| Depth         | Time Spent(s) |
| ------------- |:-------------:|
| 3             | ~1.41         |
| 4             | ~1.97         |
| 5             | ~4.84         | -->
