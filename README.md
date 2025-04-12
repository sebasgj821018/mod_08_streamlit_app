# 📊 Streamlit App - Módulo 08 | Creación y Despliegue de Aplicaciones en Streamlit.

Esta aplicación desarrollada con **Streamlit** forma parte del Módulo 08 del Máster en Python Avanzado Aplicado al Deporte. 
Permite la exploración interactiva de archivos CSV, visualización de datos desde la API pública de la CONMEBOL y consultas SQL sobre una base de datos local, todo protegido mediante un sistema de autenticación personalizado.

---

## 🚀 Funcionalidades principales

### 🔐 Autenticación de Usuario
- Control de acceso con usuario y contraseña.
- Sesión de bienvenida y cierre de sesión disponible desde el menú lateral.

### 📂 Análisis de CSV Local
- Carga de archivos `.csv` de hasta 200MB.
- Visualización tabular de los datos cargados.
- Gráficos automáticos para:
  - Goles por jugador
  - Asistencias por jugador
  - Comparación entre Goles reales y Goles esperados (xG)

### 🌐 Consulta de API CONMEBOL
- Conexión a la API `https://conmebol-api.vercel.app`
- Posibilidad de seleccionar entre tres tipos de información:
  - Clasificación
  - Resultados recientes
  - Próximos partidos
- Visualización de datos en tablas y gráficos comparativos por país.

### 🗃️ Consulta a Base de Datos SQLite
- Consulta interactiva sobre una base de datos local (`jugadores.db`)
- Editor de sentencias SQL personalizadas con resultados en tabla.

---

## 🧪 Estructura del proyecto

mod_08_streamlit_app/ ├── app.py # Archivo principal ├── pages/ # Páginas del dashboard │ ├── page_1.py # Análisis CSV │ ├── page_2.py # Consulta API │ └── page_sql.py # Consulta SQL ├── utils/ # Funciones auxiliares │ └── funciones.py ├── data/ # Archivos de datos locales │ └── jugadores.db ├── .streamlit/ # Configuración del menú lateral │ └── config.toml ├── generar_hash_bcrypt.py # Script para generar hashes de contraseñas ├── .env # Archivo con variables de entorno ├── requirements.txt # Dependencias └── README.md # Este archivo


---

## ⚙️ Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/sebasgj821018/mod_08_streamlit_app.git
cd mod_08_streamlit_app

## Instalar dependencias

pip install -r requirements.txt


## Ejecutar la aplicación:

streamlit run app.py

Despliegue en Streamlit Cloud
Para desplegar esta aplicación en Streamlit Cloud:

Sube todo el contenido del proyecto a un repositorio de GitHub.

Inicia sesión en https://streamlit.io/cloud.

Selecciona tu repositorio y configura app.py como archivo principal.

## Autor

Sebastián Gaviria Jaramillo

📍 Medellín, Colombia

🎓 Máster en Python Avanzado Aplicado al Deporte

🔗 GitHub: @sebasgj821018