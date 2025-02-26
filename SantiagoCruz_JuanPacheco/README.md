# Proyecto de Reconstrucción 3D con COLMAP y Open3D

## Requisitos

Para ejecutar este proyecto, necesitas tener instalados los siguientes paquetes de Python:

- `numpy`
- `matplotlib`
- `opencv-python`
- `pycolmap`
- `open3d`
- `tqdm`
- `enlighten`

Puedes instalarlos usando `pip`:

```sh
pip install numpy matplotlib opencv-python pycolmap open3d tqdm enlighten
```

## Pasos Realizados

### 1. Carga de Datos

Se cargan las imágenes desde el directorio [`imagenes`](imagenes):


### 2. Exploración

Se realiza una exploración inicial de las imágenes cargadas para verificar su calidad y características.

### 3. Preprocesamiento

Se leen las imágenes y se realizan tranformaciones de contraste, brillo y se usa un ROI.


### 4. Extracción de Características y Emparejamiento

Se utiliza SIFT como detector de características y FLANN como emparejador

### 5. Cálculo de Matrices

Se realiza el cálculo de las matrices y de las posiciones relativas de las cámaras.

### 6. Reconstrucción 3D

Se usa pycolmap


## Autores

- Juan Pacheco
- Santiago Cruz