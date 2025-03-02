import os
import pycolmap
import time
from PIL import Image

images_path = "imagenes"
output_path = "salida"
sparse_path = os.path.join(output_path, "sparse", "0")
dense_path = os.path.join(output_path, "dense")
database_path = os.path.join(output_path, "database.db")
ply_output_path = os.path.join(output_path, "modelo.ply")

# Asegurar que las carpetas existen
os.makedirs(output_path, exist_ok=True)
os.makedirs(os.path.join(output_path, "sparse"), exist_ok=True)
os.makedirs(dense_path, exist_ok=True)

# Reducir tamaño de imágenes si son muy grandes 
def resize_images(image_folder, max_size=1024):
    for img_name in os.listdir(image_folder):
        img_path = os.path.join(image_folder, img_name)
        if img_path.lower().endswith(('.jpg', '.png', '.jpeg')):
            img = Image.open(img_path)
            img.thumbnail((max_size, max_size))
            img.save(img_path)
            print(f"Imagen reducida: {img_name}")

resize_images(images_path)

# Verificar si hay imágenes en la carpeta
image_files = [f for f in os.listdir(images_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
if not image_files:
    raise Exception("No se encontraron imágenes en la carpeta. Verifica el directorio y el formato.")

print(f" Se encontraron {len(image_files)} imágenes en '{images_path}'.")

# Limpiar base de datos si ya existe
db_files = ["database.db", "database.db-shm", "database.db-wal"]
for f in db_files:
    path = os.path.join(output_path, f)
    if os.path.exists(path):
        os.remove(path)

try:
    #  1. Extraer características SIFT (configuración correcta)
    print(" Extrayendo características ")
    
    sift_options = pycolmap.SiftExtractionOptions()
    sift_options.num_threads = -1
    
    pycolmap.extract_features(
        database_path=database_path,
        image_path=images_path,
        sift_options=sift_options
    )
    time.sleep(2)

    #  Verificar que la base de datos no esté vacía
    if os.path.getsize(database_path) < 5000:  
        raise Exception(" La base de datos sigue vacía después de extraer características.")

    # 2. Emparejamiento de imágenes (Exhaustivo)
    print(" Emparejando imágenes")
    pycolmap.match_exhaustive(database_path=database_path)
    time.sleep(2)

    #  3. Reconstrucción incremental (Sparse)
    print(" Ejecutando reconstrucción incremental...")
    pycolmap.incremental_mapping(
        database_path=database_path,
        image_path=images_path,
        output_path=os.path.join(output_path, "sparse")
    )
    time.sleep(2)

    #  Verificar si la reconstrucción fue exitosa
    if not os.listdir(sparse_path):
        raise Exception(" La reconstrucción incremental no generó datos. Verifica las imágenes y el proceso.")

    #  4. Convertir la nube de puntos a PLY
    print(" Exportando modelo a PLY...")
    reconstruction = pycolmap.Reconstruction(sparse_path)
    reconstruction.export_PLY(ply_output_path)

    print(f" ¡Reconstrucción completada! Modelo guardado en: {ply_output_path}")

    #  (Opcional) Reconstrucción Densa
    if True:  # Cambia a False si no quieres hacer la nube densa
        print(" Generando reconstrucción densa...")

        # Generar imágenes sin distorsión
        pycolmap.undistort_images(
            image_path=images_path,
            input_path=sparse_path,
            output_path=dense_path
        )
        time.sleep(2)

        # Configurar opciones para stereo_fusion sin 'check_num_pixels'
        fusion_options = pycolmap.StereoFusionOptions()
        fusion_options.min_num_pixels = 5  # Reduce el mínimo de píxeles requeridos
        fusion_options.max_num_pixels = 500000  # Asegura un buen número de puntos

        # Fusionar nube de puntos densa con stereo_fusion
        dense_ply_output = os.path.join(dense_path, "modelo_denso.ply")

        pycolmap.stereo_fusion(
            output_path=dense_ply_output,              # Ruta de salida del archivo PLY resultante
            workspace_path=dense_path,                 # Ruta de trabajo donde se encuentran los archivos generados
            workspace_format='COLMAP',                 # Formato del espacio de trabajo
            pmvs_option_name='option-all',             # Opciones PMVS
            input_type='geometric',                   # Tipo de entrada (geométrica por defecto)
            options=fusion_options                     # Opciones de fusión personalizadas
        )

        print(f"Nube densa guardada en: {dense_ply_output}")

except Exception as e:
    print(f"Error durante la reconstrucción: {e}")
