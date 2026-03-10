import streamlit as st
import pydeck as pdk
import coletar_obras_pncp

st.title("🏗️ Obras Públicas Reais")

df = coletar_obras_pncp.buscar_obras()

if df.empty:

    st.warning("Não foi possível carregar dados do PNCP.")

else:

    st.dataframe(df.head(20))
