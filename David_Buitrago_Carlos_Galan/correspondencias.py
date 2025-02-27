import cv2
import numpy as np
import os
import pycolmap

def preprocesar_imagen_gpu(imagen):
    """
    Convierte la imagen a escala de grises, mejora el contraste y reduce el ruido.
    Utiliza OpenCL (UMat) para acelerar las dos primeras operaciones en la GPU y luego descarga
    la imagen para aplicar fastNlMeansDenoising en la CPU.
    """
    gpu_imagen = cv2.UMat(imagen)
    if len(imagen.shape) == 3:
        gpu_imagen = cv2.cvtColor(gpu_imagen, cv2.COLOR_BGR2GRAY)
    gpu_imagen = cv2.equalizeHist(gpu_imagen)
    imagen_temp = gpu_imagen.get()
    imagen_procesada = cv2.fastNlMeansDenoising(imagen_temp, None, h=10)
    return imagen_procesada

def preprocesar_imagen(imagen):
    """
    Versión original sin GPU: convierte la imagen a escala de grises, mejora el contraste y reduce el ruido.
    """
    if len(imagen.shape) == 3:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    imagen = cv2.equalizeHist(imagen)
    imagen = cv2.fastNlMeansDenoising(imagen, None, h=10)
    return imagen

def cargar_imagenes(directorio, usar_gpu=False):
    """
    Carga las imágenes de un directorio dado y aplica el preprocesamiento.
    Si usar_gpu es True, utiliza la función con procesamiento en GPU.
    """
    imagenes = []
    nombres = []
    for archivo in os.listdir(directorio):
        if archivo.lower().endswith(('.jpg', '.png', '.jpeg')):
            ruta_imagen = os.path.join(directorio, archivo)
            imagen = cv2.imread(ruta_imagen)
            if imagen is not None:
                if usar_gpu:
                    imagen = preprocesar_imagen_gpu(imagen)
                else:
                    imagen = preprocesar_imagen(imagen)
                imagenes.append(imagen)
                nombres.append(archivo)
            else:
                print(f'Error al cargar la imagen: {archivo}')
    return imagenes, nombres

def cargar_imagenes_directo(directorio):
    """
    Carga directamente las imágenes desde el directorio sin aplicar preprocesamiento.
    """
    imagenes = []
    nombres = []
    for archivo in os.listdir(directorio):
        if archivo.lower().endswith(('.jpg', '.png', '.jpeg')):
            ruta_imagen = os.path.join(directorio, archivo)
            imagen = cv2.imread(ruta_imagen)
            if imagen is not None:
                imagenes.append(imagen)
                nombres.append(archivo)
            else:
                print(f'Error al cargar la imagen: {archivo}')
    return imagenes, nombres

def guardar_imagenes(imagenes, nombres, directorio_salida):
    """
    Guarda las imágenes procesadas en el directorio de salida.
    Si el directorio no existe, se crea.
    """
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)
    
    for idx, (img, nombre) in enumerate(zip(imagenes, nombres)):
        nombre_salida = f"proc_{nombre}"
        ruta_salida = os.path.join(directorio_salida, nombre_salida)
        cv2.imwrite(ruta_salida, img)
        print(f'Imagen guardada: {ruta_salida}')

def detectar_caracteristicas(imagen, metodo="SIFT"):
    """
    Detecta puntos clave y extrae descriptores usando SIFT u ORB.
    Retorna los keypoints y descriptores.
    """
    metodo = metodo.upper()
    if metodo == "SIFT":
        detector = cv2.SIFT_create()
    elif metodo == "ORB":
        detector = cv2.ORB_create() 
    else:
        raise ValueError("Método no soportado. Use 'SIFT' o 'ORB'.")
    
    keypoints, descriptores = detector.detectAndCompute(imagen, None)
    return keypoints, descriptores

def emparejar_caracteristicas(imagen1, imagen2, metodo="SIFT", ratio=0.75):
    """
    Empareja características entre dos imágenes utilizando BFMatcher y un filtro ratio test.
    Retorna la imagen resultante con los matches dibujados.
    """
    kp1, des1 = detectar_caracteristicas(imagen1, metodo)
    kp2, des2 = detectar_caracteristicas(imagen2, metodo)
    
    if metodo.upper() == "SIFT":
        norm = cv2.NORM_L2
    elif metodo.upper() == "ORB":
        norm = cv2.NORM_HAMMING
    
    bf = cv2.BFMatcher(norm)
    matches = bf.knnMatch(des1, des2, k=2)
    
    good = []
    for m, n in matches:
        if m.distance < ratio * n.distance:
            good.append(m)
    
    matched_img = cv2.drawMatches(imagen1, kp1, imagen2, kp2, good, None, flags=2)
    return matched_img

def estimar_geometria(imagen1, imagen2):
    """
    Dado un par de imágenes, se detectan características usando SIFT, se emparejan los descriptores,
    se estima la matriz fundamental con RANSAC, se calcula la matriz esencial (usando una calibración
    supuesta) y se descompone en rotación y traslación de la cámara.
    """
    # Detectar características con SIFT en ambas imágenes
    kp1, des1 = detectar_caracteristicas(imagen1, metodo="SIFT")
    kp2, des2 = detectar_caracteristicas(imagen2, metodo="SIFT")
    
    # Emparejar descriptores usando BFMatcher con ratio test
    bf = cv2.BFMatcher(cv2.NORM_L2)
    matches_knn = bf.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matches_knn:
        if m.distance < 0.75 * n.distance:
            good.append(m)
    
    if len(good) < 8:
        print("No hay suficientes matches para estimar la geometría robustamente.")
        return None, None, None, None
    
    # Extraer coordenadas de los matches
    pts1 = np.float32([kp1[m.queryIdx].pt for m in good])
    pts2 = np.float32([kp2[m.trainIdx].pt for m in good])
    
    # Calcular la matriz fundamental con RANSAC
    F, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_RANSAC)
    print("Matriz Fundamental:")
    print(F)
    
    # Filtrar correspondencias inliers
    pts1_inliers = pts1[mask.ravel() == 1]
    pts2_inliers = pts2[mask.ravel() == 1]
    
    # Suponer una matriz de calibración (K)
    # Estos valores deben corresponder a la cámara usada; aquí se estima a partir de las dimensiones de la imagen
    h, w = imagen1.shape[:2]
    f = 1.2 * w   # Valor heurístico para la longitud focal
    cx = w / 2
    cy = h / 2
    K = np.array([[f, 0, cx],
                  [0, f, cy],
                  [0, 0, 1]])
    
    # Calcular la matriz esencial a partir de la matriz fundamental y K
    E = K.T.dot(F).dot(K)
    print("Matriz Esencial:")
    print(E)
    
    # Descomponer la matriz esencial en rotación (R) y traslación (t)
    retval, R, t, mask_pose = cv2.recoverPose(E, pts1_inliers, pts2_inliers, K)
    print("Rotación:")
    print(R)
    print("Traslación:")
    print(t)
    
    return F, E, R, t

def main():
    # Habilitar OpenCL si está disponible
    if cv2.ocl.haveOpenCL():
        cv2.ocl.setUseOpenCL(True)
        print("OpenCL habilitado, se usará la GPU AMD.")
    else:
        print("OpenCL no está disponible, se usará la CPU.")
    
    # Directorios de entrada y salida
    directorio_entrada = os.path.abspath(os.path.join(os.path.dirname(__file__), '', 'imagenes'))
    directorio_salida = os.path.abspath(os.path.join(os.path.dirname(__file__), '', 'imagenes_procesadas'))
    directorio_correspondencias = os.path.abspath(os.path.join(os.path.dirname(__file__), '', 'correspondencias'))
    
    # Si existen imágenes procesadas en el directorio de salida, cárgalas directamente
    if os.path.exists(directorio_salida) and any(f.lower().endswith(('.jpg', '.png', '.jpeg'))
                                                for f in os.listdir(directorio_salida)):
        print("Se encontraron imágenes preprocesadas, cargando directamente del directorio de salida.")
        imagenes, nombres = cargar_imagenes_directo(directorio_salida)
    else:
        print("No se encontraron imágenes preprocesadas, cargando y procesando imágenes de entrada.")
        imagenes, nombres = cargar_imagenes(directorio_entrada, usar_gpu=True)
        guardar_imagenes(imagenes, nombres, directorio_salida)
    
    print(f'Se cargaron {len(imagenes)} imágenes')
    

    # Detectar y dibujar puntos clave en la primera imagen (ejemplo)
    if imagenes:
        kp, _ = detectar_caracteristicas(imagenes[0], metodo="ORB")
        img_kp = cv2.drawKeypoints(imagenes[0], kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        # Guardar los puntos clave en la misma carpeta que las correspondencias
        ruta_kp = os.path.join(directorio_correspondencias, "puntos_clave.jpg")
        cv2.imwrite(ruta_kp, img_kp)
        print(f'Imagen con puntos clave guardada: {ruta_kp}')
    
    # Emparejar características entre la primera y la segunda imagen (si existen)
    if len(imagenes) >= 2:
        img_matches = emparejar_caracteristicas(imagenes[0], imagenes[1], metodo="SIFT")
        # Crear el directorio para guardar las correspondencias si no existe
        if not os.path.exists(directorio_correspondencias):
            os.makedirs(directorio_correspondencias)
        ruta_matches = os.path.join(directorio_correspondencias, "correspondencias.jpg")
        cv2.imwrite(ruta_matches, img_matches)
        print(f'Imagen con correspondencias guardada: {ruta_matches}')
    else:
        print("No hay suficientes imágenes para emparejar características.")
    
    # Estimar la geometría entre la primera y la segunda imagen (si existen)
    if len(imagenes) >= 2:
        F, E, R, t = estimar_geometria(imagenes[0], imagenes[1])
        print("Matriz Fundamental:")
        print(F)
        print("Matriz Esencial:")
        print(E)
        print("Rotación:")
        print(R)
        print("Traslación:")
        print(t)
    else:
        print("No hay suficientes imágenes para estimar la geometría.")

if __name__ == '__main__':
    main()