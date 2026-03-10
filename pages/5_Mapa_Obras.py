import streamlit as st
import pandas as pd
import obras_publicas

st.title("🗺️ Mapa de Obras Públicas")

st.write("""
Visualização de investimentos públicos no mapa.

Mostra:
- localização de obras
- valor investido
- empresa responsável
""")

df = obras_publicas.carregar_obras()

st.subheader("📋 Lista de obras")

st.dataframe(df)

st.subheader("📍 Localização das obras")

mapa = df.rename(columns={
    "lat":"latitude",
    "lon":"longitude"
})

st.map(mapa)

st.subheader("💰 Valor por obra")

st.bar_chart(df.set_index("obra")["valor"])
