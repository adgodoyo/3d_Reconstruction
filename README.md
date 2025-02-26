# Guía Rápida del Código de Visión

Este documento proporciona una visión general del código incluido en el archivo Jupyter Notebook, detallando las librerías utilizadas y un paso a paso resumido del flujo del programa.

## Librerías Utilizadas

El código hace uso de las siguientes librerías de Python:

```python
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.feature import SIFT
import pycolmap
```

Estas librerías son esenciales para el procesamiento de imágenes, la detección de características y la visualización de resultados.

## Paso a Paso del Código

### 1. Carga de Imagen
- Se lee la imagen desde un archivo usando OpenCV (`cv2.imread`).
- Se convierte la imagen a escala de grises para facilitar el procesamiento.

### 2. Aplicación del Detector de Características SIFT
- Se inicializa el detector SIFT.
- Se detectan y extraen características clave de la imagen.
- Se almacenan los descriptores generados.

### 3. Visualización de Resultados
- Se dibujan los puntos clave detectados en la imagen.
- Se muestra la imagen con los puntos clave resaltados utilizando Matplotlib.

### 4. Matrices
- Se calculan las matrices solicitadas y se reutiliza el código de chessboard

### 5. Guardado de Resultados
- Se guarda la imagen procesada con las características detectadas en un archivo de salida.

## Cómo Ejecutar el Código

Para ejecutar este código en un entorno Jupyter Notebook, asegúrate de tener instaladas las librerías necesarias. Puedes instalarlas con:

```bash
pip install numpy opencv-python matplotlib scikit-image
```

Luego, ejecuta cada celda en orden dentro del notebook.

## Notas Adicionales
- OpenCV se usa para el manejo de imágenes y detección de características.
- SIFT es un método efectivo para la detección de puntos clave en imágenes.
- Matplotlib se emplea para visualizar los resultados de manera gráfica.

---

Este README proporciona una referencia rápida para comprender el código y su ejecución.
