Reconstrucción 3D con Structure from Motion (SfM) en Jupyter Notebook

Este repositorio contiene un proyecto de reconstrucción 3D utilizando Structure from Motion (SfM) implementado en un Jupyter Notebook. Se utilizan bibliotecas de procesamiento de imágenes y nubes de puntos para visualizar una reconstrucción tridimensional preexistente a partir de un conjunto de imágenes cargadas.

Contenido

Preprocesamiento de Imágenes: Carga y conversión a escala de grises.

Detección y Correspondencia de Características: Uso de SIFT y FLANN para encontrar coincidencias entre imágenes.

Estimación de la Matriz Esencial: Cálculo de la matriz fundamental y esencial para la estimación de la geometría de la cámara.

Reconstrucción 3D: Triangulación de puntos y generación de la nube de puntos.

Requisitos

Antes de ejecutar el notebook, instala las siguientes dependencias:

pip install opencv-python numpy matplotlib scipy open3d

Uso

Ejecuta el notebook paso a paso.

Visualiza la reconstrucción 3D ya generada.

Nota: Este proyecto no genera reconstrucciones nuevas a partir de imágenes distintas a las cargadas, solo permite visualizar la reconstrucción existente.

Autor

José Daniel Mejía