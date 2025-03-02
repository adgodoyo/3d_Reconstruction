# Taller 1 - Procesamiento de Imágenes

Este repositorio contiene un notebook de Jupyter titulado `taller1.ipynb`, que aborda el procesamiento de imágenes utilizando diversas técnicas computacionales.


## Requisitos
Para ejecutar el notebook correctamente, se recomienda instalar las siguientes dependencias:

```bash
pip install opencv-python numpy matplotlib colmap scipy scikit-image
```

Este proyecto utiliza **COLMAP-CUDA**, una herramienta de reconstrucción 3D basada en visión por computadora

### Pasos realizados en el taller

1. **Carga de imágenes**: Se importaron imágenes de prueba para aplicar los algoritmos de procesamiento.
2. **Preprocesamiento**: Aplicamos filtros para mejorar la calidad de las imágenes y eliminar ruido.
3. **Extracción de características**: Se detectaron puntos clave con SIFT y ORB.
4. **Emparejamiento de características**: Se utilizaron métodos como FLANN y BFMatcher para encontrar correspondencias entre imágenes.
5. **Reconstrucción con COLMAP**: Se procesaron las imágenes en COLMAP para generar un modelo 3D.
6. **Visualización**: Se hizo la Visualización de la nube de puntos por medio de un archivo pyl

## Contribución
Si deseas mejorar este proyecto, puedes hacer un fork y enviar pull requests con mejoras en el código o documentación.

## Autores
Johan Santiago Caro Valencia & Juan Sebastian Rodriguez Salazar

