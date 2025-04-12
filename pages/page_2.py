import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

def mostrar():
    st.title("📡 Consulta de Datos desde la API de la CONMEBOL")

    # Diccionario para construir URL automáticamente
    opciones = {
        "Clasificación": "classification",
        "Próximos partidos": "matches",
        "Resultados recientes": "results"
    }

    seleccion = st.selectbox("Selecciona el tipo de información:", list(opciones.keys()))
    endpoint = opciones[seleccion]
    url = f"https://conmebol-api.vercel.app/api/{endpoint}"
    st.code(f"🔗 URL consumida: {url}")

    try:
        response = requests.get(url)
        data = response.json()

        if seleccion == "Resultados recientes":
            jornada = list(data.keys())[0]
            resultados = data[jornada]
            df = pd.json_normalize(resultados)

            # Convertir columnas numéricas
            columnas_numericas = ["first_team.goals", "second_team.goals"]
            for col in columnas_numericas:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors="coerce")

            st.subheader("📊 Resultados recientes")
            st.dataframe(df)

            # Filtros
            paises = pd.unique(df[["first_team.country", "second_team.country"]].values.ravel())
            pais = st.selectbox("Filtrar por país", ["Todos"] + list(paises))
            if pais != "Todos":
                df = df[(df["first_team.country"] == pais) | (df["second_team.country"] == pais)]

            # Goles por país
            goles_df = pd.DataFrame()
            goles_df["País"] = pd.concat([df["first_team.country"], df["second_team.country"]])
            goles_df["Goles"] = pd.concat([df["first_team.goals"], df["second_team.goals"]])
            goles_agrupados = goles_df.groupby("País").sum().sort_values("Goles", ascending=False)

            st.markdown("### 🥅 Goles por País")
            fig1, ax1 = plt.subplots()
            ax1.bar(goles_agrupados.index, goles_agrupados["Goles"])
            ax1.set_ylabel("Goles")
            ax1.set_xlabel("País")
            ax1.set_title("Total de goles por país")
            ax1.tick_params(axis='x', rotation=45)
            st.pyplot(fig1)

            # Top 5
            st.markdown("### 🏆 Top 5 Países Goleadores")
            st.bar_chart(goles_agrupados.head(5))

        elif seleccion == "Clasificación":
            if "results" in data:
                df = pd.DataFrame(data["results"])

                # Conversión de columnas
                numericas = ["position", "points", "matches_played", "won", "tied", "losses", "goal_difference"]
                for col in numericas:
                    if col in df.columns:
                        df[col] = pd.to_numeric(df[col], errors="coerce")

                st.subheader("📊 Tabla de Clasificación")
                st.dataframe(df)

                st.markdown("### 📈 Puntos por País")
                df_sorted = df.sort_values("points", ascending=False)
                fig2, ax2 = plt.subplots()
                ax2.barh(df_sorted["country"], df_sorted["points"], color="orange")
                ax2.set_xlabel("Puntos")
                ax2.set_title("Clasificación CONMEBOL")
                ax2.invert_yaxis()
                st.pyplot(fig2)
            else:
                st.warning("⚠️ El JSON no contiene el campo 'results'")

        elif seleccion == "Próximos partidos":
            jornadas = list(data.keys())
            jornada_sel = st.selectbox("Selecciona una jornada", jornadas)

            if jornada_sel in data:
                partidos = data[jornada_sel]
                df = pd.DataFrame(partidos)
                df["date"] = pd.to_datetime(df["date"], errors="coerce")

                st.subheader(f"📅 Partidos - {jornada_sel}")
                st.dataframe(df)

                equipos = pd.concat([df["first_team"], df["second_team"]])
                conteo = equipos.value_counts().reset_index()
                conteo.columns = ["Equipo", "Apariciones"]

                st.markdown("### 🔢 Apariciones por Equipo")
                fig3, ax3 = plt.subplots()
                ax3.bar(conteo["Equipo"], conteo["Apariciones"], color="blue")
                ax3.set_ylabel("Cantidad de partidos")
                ax3.set_xlabel("Equipo")
                ax3.set_title(f"Apariciones por equipo - {jornada_sel}")
                ax3.tick_params(axis='x', rotation=45)
                st.pyplot(fig3)
            else:
                st.warning("⚠️ La jornada seleccionada no tiene datos válidos")

    except Exception as e:
        st.error(f"❌ Error al procesar la API: {e}")
