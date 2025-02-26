import open3d as o3d
import matplotlib.pyplot as plt

# Load the dense point cloud
dense_ply_path = "JulianaBermudez_SofiaDuarte/src/colmapReconstruction/dense/0/fused.ply"
pcd = o3d.io.read_point_cloud(dense_ply_path)

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])
