## NYU Urban LiDAR and Remote Sensing Data Structure Team Project

### Keywords: 

Urban Studies, Storage and Access of Point Cloud File, Data Structure

### Layout
```
.
├── data/    # point cloud data files in las and csv formats and some visualizations of them in gephi_img and img folders
│   ├── House/
│   ├── Light Pole/
│   └── Tree/
├── images/    # images to be displayed in README.md
├── visualizations/    # contains produced data visualizations in the chosen data structures
├── tests/    # several old python codes for implementing those visualizations
│   ├── env/    # the environment for running the test codes
├── Octree-Visual.ipynb/    # code for creating node.csv and edge.csv for creating octree visualization in Gephi and some topological data analysis
├── KDTree-Standard-Visual.ipynb/    # code for creating node.csv and edge.csv for creating standard K-D tree visualization in Gephi and doing some topological data analysis
├── KDTree-Adaptive-Visual.ipynb/    # code for creating node.csv and edge.csv for creating adaptive K-D tree (axis-split based on variance) visualization in Gephi and some topological data analysis
├── RTree-Visual.ipynb/    # (incomplete) code for creating R tree visualization using matplotlib
└── README.md
```

### Data Source:
> Laefer, D.F., Vo, A.-V. 2020. “2019 LiDAR Data Collection for Sunset Park” NYU Spatial Data Repository, Brooklyn, NY doi.org/10.17609/4cpx-2h33/. Available at http://hdl.handle.net/2451/60458

<img src="images/data.png" width="400" height="300">

### Sample Octree (with depth=3) Visualization for a House Point Cloud:

<img src="images/incomplete_octree_visual.png" width="400" height="400">
