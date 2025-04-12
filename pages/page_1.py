import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def mostrar():
    st.title("Análisis de CSV Local")

    file = st.file_uploader("📂 Carga un archivo CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.dataframe(df)

        st.markdown("### 📊 Gráfico de goles por jugador")
        if 'jugador' in df.columns and 'goles' in df.columns:
            st.bar_chart(data=df, x="jugador", y="goles")

        st.markdown("### 🎯 Asistencias por jugador")
        if 'asistencias' in df.columns:
            st.bar_chart(data=df, x="jugador", y="asistencias")

        st.markdown("### 🔁 Comparación Goles vs xG")

        if 'xG' in df.columns:
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.bar(df['jugador'], df['goles'], label='Goles', alpha=0.7)
            ax.bar(df['jugador'], df['xG'], label='xG', alpha=0.7)
            ax.set_ylabel("Cantidad")
            ax.set_title("Comparación de Goles vs xG por Jugador")
            ax.legend()
            st.pyplot(fig)

        st.markdown("✅ Análisis listo. Puedes usar otras páginas desde el menú lateral.")
    else:
        st.info("💡 Carga un archivo CSV con las columnas correctas para comenzar.")
