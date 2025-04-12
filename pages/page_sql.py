import streamlit as st
import pandas as pd
import sqlite3

def mostrar():
    st.title("🗄️ Consulta a Base de Datos SQLite")

    db_path = st.text_input("📁 Ruta del archivo SQLite", "data/jugadores.db")

    if db_path:
        try:
            conn = sqlite3.connect(db_path)
            query = st.text_area("📝 Escribe tu consulta SQL", "SELECT * FROM jugadores LIMIT 10")

            if st.button("Ejecutar consulta"):
                df = pd.read_sql_query(query, conn)
                st.dataframe(df)

        except Exception as e:
            st.error(f"⚠️ Error al conectar a la base de datos: {e}")
