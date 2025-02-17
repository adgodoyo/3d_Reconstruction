# 🏗️ Reconstrucción 3D con Structure from Motion (SfM)

---

## 📖 Descripción  

En este repositorio, los estudiantes implementarán un sistema de reconstrucción 3D utilizando **Structure from Motion (SfM)**. Cada equipo tomará imágenes de un objeto o escena y generará un modelo tridimensional a partir de ellas.  

Los estudiantes pueden utilizar **PyCOLMAP** o **VGGSfM** para realizar la reconstrucción.  

---

## 📋 Instrucciones de Entrega  

### **1️⃣ Clonar el Repositorio**  
Cada grupo debe clonar este repositorio en su máquina local:  

```bash 
git clone https://github.com/tu_usuario/reconstruccion-3d-sfm.git
cd reconstruccion-3d-sfm
```

### **2️⃣ Crear una Nueva Rama**  
Cada grupo debe trabajar en su propia rama, nombrada de la siguiente manera:  
📌 **Formato:** `grupoX_nombre1_nombre2`  

Ejemplo:  

```bash
git checkout -b grupo1_juan_maria
git push origin grupo1_juan_maria
```

### **3️⃣ Estructura del Proyecto**  

Cada equipo debe organizar su entrega con la siguiente estructura:  

📌 **Formato:** `Integrante1_Integrante2/`  

Ejemplo para un grupo conformado por "JuanOrtiz" y "MaríaGodoy":  

```bash
📂 reconstruccion-3d-sfm/
│── 📁 JuanOrtiz_MariaGodoy/         # Carpeta del grupo
│   │── 📁 imagenes/       # Carpeta con las imágenes usadas
│   │── 📂 src/            # Código en Python
│   │── 📜 video.mpeg     # Explicación breve del proceso y resultados
│   │── 📜 README.md       # Explicación breve de su implementación con los resultados
│── 📁 OtroGrupo/          # Otra entrega de un equipo distinto
│── 📜 README.md           # Archivo principal del repositorio
```
El nombre de la carpeta no puede ir con espacios, puntos y considere que la primera letra del nombre y apellido va en mayúscula (el resto en minúscula)

📌 **Nota:** Todas las imágenes utilizadas deben estar en la carpeta `imagenes/`.  

---

## 🛠️ Pasos Generales para la Implementación  

### **1️⃣ Captura de Imágenes**  
- Tomar entre **10-20 imágenes** desde diferentes ángulos.  
- Asegurar buena iluminación y enfoque.  
- Guardarlas en `imagenes/`.  

### **2️⃣ Preprocesamiento**  
- Convertir imágenes a escala de grises.  
- Aplicar filtros para mejorar contraste si es necesario.  

### **3️⃣ Detección y Correspondencia de Características**  
- Usar **SIFT, ORB o SuperPoint**.  
- Emparejar puntos clave entre imágenes.  

### **4️⃣ Estimación de Matriz Fundamental y Matriz Esencial**  
- Calcular la **matriz fundamental** con RANSAC.  
- Obtener la **posición relativa de las cámaras**.  

### **5️⃣ Reconstrucción 3D con SfM**  

#### 🔹 **Opción 1: PyCOLMAP**  
1. Instalar COLMAP y PyCOLMAP.  
2. Ejecutar el proceso en la terminal:  

```bash
colmap feature_extractor --database_path db.db --image_path ./imagenes
colmap mapper --database_path db.db --image_path ./imagenes --output_path ./output
``` 

3. Exportar el modelo y visualizarlo en Open3D.  

#### 🔹 **Opción 2: VGGSfM**  
1. Descargar el modelo preentrenado.  
2. Ejecutar la reconstrucción en Python.  

---

## 📤 Subida de Archivos  

### **1️⃣ Agregar los archivos al repositorio**  
Una vez completado el trabajo, subir los archivos al repositorio en la rama del equipo:  

```bash
git add .
git commit -m "Entrega del proyecto por grupo1_juan_maria"
git push origin grupo1_juan_maria
```

### **2️⃣ Crear un Pull Request (PR)**  
1. Ir al repositorio en GitHub.  
2. Hacer clic en **"Pull Requests"** → **"New Pull Request"**.  
3. Seleccionar **`grupo1_juan_maria` → `main`**.  
4. Agregar una breve descripción y enviar la solicitud.  

---



