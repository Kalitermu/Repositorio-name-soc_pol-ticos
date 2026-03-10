import streamlit as st
import mapa_sp

st.title("🗺️ Mapa de Risco Fiscal - São Paulo")

df = mapa_sp.dados_mapa()

st.subheader("📊 Cidades analisadas")

st.dataframe(df)

st.subheader("🌎 Visualização no mapa")

mapa = df.rename(columns={
    "lat":"latitude",
    "lon":"longitude"
})

st.map(mapa)
