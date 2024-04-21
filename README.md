## NYU Urban LiDAR and Remote Sensing Data Structure Team Project

### Keywords: 

Urban Studies, Storage and Access of Point Cloud File, Data Structure

### Layout
```
.
├── data/                  # Point cloud data files (.las, .csv) and data visualization (.gephi)
│   ├── House/
│   ├── Light Pole/
│   └── Tree/
├── images/                # Displayed images
│   ├── visualizations/    # Data visualizations/data flowers in Octree and K-D Tree data structures
├── tests/                 # Unused/Old python codes for data visualizations
│   ├── env/               # The environment for running test codes
├── Octree-Visual.ipynb/   # Octree Implementation and Visualization
├── KDTree-Visual.ipynb/   # K-D Tree Implementation and Visualization
├── RTree-Visual.ipynb/    # (incomplete) code for creating R tree visualization using matplotlib
└── README.md
```

### Data Source:
> Laefer, D.F., Vo, A.-V. 2020. “2019 LiDAR Data Collection for Sunset Park” NYU Spatial Data Repository, Brooklyn, NY doi.org/10.17609/4cpx-2h33/. Available at http://hdl.handle.net/2451/60458

<img src="images/data.png" width="400" height="300">

### Sample Octree (with depth=3) Visualization for a House Point Cloud:

<img src="images/incomplete_octree_visual.png" width="400" height="400">
