import streamlit as st
import pandas as pd
import mapa_corrupcao_brasil

st.title("🌎 Radar Nacional de Corrupção")

df = mapa_corrupcao_brasil.dados_mapa()

st.subheader("📊 Ranking de risco")

st.dataframe(df.sort_values("risco",ascending=False))

st.subheader("🛰️ Mapa nacional")

mapa = df.rename(columns={
    "lat":"latitude",
    "lon":"longitude"
})

st.map(mapa)

st.subheader("📈 Distribuição de risco")

st.bar_chart(df.set_index("cidade")["risco"])
