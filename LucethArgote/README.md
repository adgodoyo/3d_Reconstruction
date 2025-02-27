# Taller 1 - Reconstrucción 3D a partir de imágenes usando Structure from Motion (SfM).

## Descripción
Implementar una reconstrucción 3D de una escena a partir de imágenes utilizando Structure from Motion (SfM) con PyCOLMAP. La primera parte está implementada en el notebook 'Reconstruccion3D_Vision.ipynb' y la segunda parte está implementada en reconstruccion3D_pycolmap.py.

## Tabla de Contenidos
- [Librerías](#librerías)
- [Calibración de la cámara](#calibración)
- [Pre-procesamiento, detección de características y emparejamiento](#preprocesamiento)
- [Matriz fundamental, escencial, rotación y traslación](#matrices)
- [Reconstrucción con PYCOLMAP](#pycolmap)
- [Autor/es](#autor)

## Librerías
Se usaron las siguientes librerías:
```sh
import shutil
import urllib.request
import zipfile
from pathlib import Path

import enlighten

import pycolmap
from pycolmap import logging

import open3d as o3d

import numpy as np
import cv2 as cv
import glob
from tqdm import tqdm
import seaborn as sns

from google.colab.patches import cv2_imshow
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
```

## Calibración de la cámara.
- Se debe hacer para obtener la matriz intrinseca de la cámara.
- Se usaron las imágenes de la carpeta '\src\chess' para calibrar la cámara.

## Pre-procesamiento, detección de características y emparejamiento.
- Se cargaron las imagenes de la carpeta 'imagenes'.
- Se usó SIFT para la detección de características.
- Se pasaron las imagenes a escala de grises, se hicieron mejoras de contraste, reducción de ruido y se corrigió la distorsión con roi y la matriz intrinseca antes calculada.
- Se hizo el emparejamiento de características con FLANN.
- Se muestran los emparejamientos obtenidos.

## Matriz fundamental, escencial, rotación y traslación
- Se calcularon estas matrices para cada emparejamiento obtenido.

## Reconstrucción con PYCOLMAP.
- Se extraen las características y se emparejan las imágenes.
- Se usa SIFT.
- Ejecuta la reconstrucción incremental.
- Registra imágenes secuencialmente.
- Genera y guarda el modelo reconstruido.
- Exporta la nube de puntos en formato PLY.
- Se visualiza la nube de puntos con Open3D.

## Autor/es.
- Luceth Argote



