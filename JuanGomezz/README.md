# Calibración de cámara

Aquí se pasan varias imágenes de un ajedrez y el resultado es una matriz en coordenadas homogéneas, las cuales tienen las propiedades intrínsecas de la cámara.

# Extraer características y matriz fundamental con geometría

Aquí se utilizan imágenes del objeto al que se le quiera hacer la reconstrucción. Primero se extraen las características de la imagen con SIFT, luego se hallan los matches con FLANN y se filtran los buenos matches. Se halla la matriz fundamental y la máscara, y a partir de eso se obtienen la rotación y traslación. Luego se hace la triangulación y se hallan los puntos 3D. Finalmente, se muestran los matches en las imágenes, la matriz fundamental, rotación, traslación y puntos 3D.

# Reconstrucción

Se utiliza la librería COLMAP para que realice lo mencionado anteriormente de manera interna y nos dé la nube de puntos 3D.

# Visualizar

Se usa la librería Open3D para ver la nube de puntos (`reconstruccion_0.py`). Puede que la reconstrucción se vea volteada por la naturaleza de las imágenes originales.
