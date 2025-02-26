import pycolmap
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the 3D reconstruction
# sfm_path = "JulianaBermudez_SofiaDuarte/src/example/sfm/0" # Obtenido con ejemplo del repo de pycolmap
sfm_path = "JulianaBermudez_SofiaDuarte/src/colmapReconstruction/sparse/0" # Obtenido con COLMAP
reconstruction = pycolmap.Reconstruction(sfm_path)

# Extract 3D points
points3D = reconstruction.points3D

# Plot the 3D points
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(
    [p.xyz[0] for p in points3D.values()],
    [p.xyz[1] for p in points3D.values()],
    [p.xyz[2] for p in points3D.values()],
    s=1, c='blue'
)

ax.set_title("Sparse 3D Point Cloud")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
