## NYUVIP-Point-Cloud-Data-Structure
### NYU Urban LiDAR and Remote Sensing (GY) Team Project

#### Create a virtual environment to run the programs in tests directory
```
python3.9 -m venv ENV_NAME
source ENV_NAME/bin/activate
pip install open3d
pip install networkx
```

Sample Point Cloud File

<img src="images/sample_data.png" width="300" height="200">

You may inspect the octree structure of the sample point cloud in Open3D.

<img src="images/test0_octree.png" width="550" height="250">

You can also inspect the octree or k-d tree structure of the file using the code in the test file, and clean the graph using Gephi.

<img src="images/test2_gephi_octree.png" width="250" height="250">
<img src="images/test2_gephi_kdtree.png" width="200" height="200">

Here is a  more complicated example with larger point cloud file in octree structure.

<img src="gephis/octree-cleaned/streetlight_chunked_octree.png" width="300" height="310">
<img src="gephis/kdtree-cleaned/streetlight_chunked_kdtree.png" width="300" height="310">