import streamlit as st
from utils.login import crear_login
from pages import page_1, page_2
import pages.page_sql as page_sql

# Configuración inicial
st.set_page_config(page_title="App Streamlit Módulo 8", layout="wide")

# Crear autenticador
authenticator = crear_login()

# Mostrar login (sin unpack)
authenticator.login(location='main')

# Evaluar estado de autenticación con session_state
if st.session_state.get("authentication_status") is True:
    authenticator.logout("Cerrar sesión", "sidebar")
    st.sidebar.success(f"Bienvenido 👋 {st.session_state['name']}")

    page = st.sidebar.selectbox("Selecciona una página", ["Análisis CSV", "Datos desde API", "Datos desde SQL"])
    if page == "Análisis CSV":
        page_1.mostrar()
    elif page == "Datos desde API":
        page_2.mostrar()
    elif page == "Datos desde SQL":
        page_sql.mostrar()

elif st.session_state.get("authentication_status") is False:
    st.error("❌ Usuario o contraseña incorrecta")

elif st.session_state.get("authentication_status") is None:
    st.warning("⚠️ Por favor ingresa tus credenciales")
