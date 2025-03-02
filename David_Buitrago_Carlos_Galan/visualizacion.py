import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

# Ruta del modelo reconstruido
ply_output_path = r"salida\modelo.ply"

#  Cargar la nube de puntos con Open3D
print("Cargando la nube de puntos...")
nube = o3d.io.read_point_cloud(ply_output_path)

#  Visualizar en Open3D
print("Mostrando la nube de puntos en Open3D...")
o3d.visualization.draw_geometries([nube])

# Convertir la nube de puntos a un array de NumPy para graficar en Matplotlib
puntos = np.asarray(nube.points)
