import streamlit as st
from modules.radar_nacional import gerar_base_nacional

st.title("🇧🇷 Ranking Nacional de Risco Fiscal")

df = gerar_base_nacional()

st.dataframe(df[[
    "cidade",
    "estado",
    "gasto_total",
    "repeticoes",
    "concentracao",
    "score_risco"
]])

st.bar_chart(df.set_index("cidade")["score_risco"])
