# Reconstrucción 3D con COLMAP  

Este proyecto realiza la reconstrucción 3D de una escena a partir de un conjunto de imágenes utilizando **COLMAP**. Se emplean algoritmos de detección de características y emparejamiento de puntos clave para generar una nube de puntos densa.

## Estructura del Proyecto

`````plaintext
📂 Alejandro Vega
  📂 imagenes  (Imágenes a color para modelar)  
  ├── 📂 imagenes bw  (Imágenes en blanco y negro para modelar)  
  ├──  📂 imagenes c   (Imágenes de calibración)
  📂 src  
  ├── reconstruccion3D.ipynb  (Notebook principal)  
  fused.ply  (Nube de puntos generada)  
  video.mkv  (Explicación del notebook en video)
`````

 ## Requisitos

 Para ejecutar el notebook se requieren tener instaladas ciertas librerías, lo cual se puede hacer con el siguiente comando:
 `````python
pip install opencv-python open3d numpy matplotlib
`````
## Desarrollo del notebook

Para realizar el modelado 3D de la escena se siguieron los siguientes pasos:
1. Carga de las imágenes con cv2
2. preprocesamiento de las imágenes con cv2
3. Cálculo de la matriz fundamental y la matriz esencial usando RANSAC
4. Extracción de características usando SIFT
5. Emparejamiento de características usando FLANN
6. Reconstrucción 3D usando COLMAP
7. Visualización del modelo 3D usando Open3d

## Autor
Alejandro Rafael Vega Saavedra
