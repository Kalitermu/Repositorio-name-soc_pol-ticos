import streamlit as st
import pandas as pd

st.title("🌎 Mapa de Risco Fiscal")

dados = pd.DataFrame({
    "cidade":["São Vicente","Praia Grande","Santos"],
    "lat":[-23.96,-24.00,-23.95],
    "lon":[-46.38,-46.41,-46.33],
    "score":[6.7,5.9,4.1]
})

def cor(score):
    if score >= 7:
        return "🔴 alto"
    elif score >= 4:
        return "🟡 médio"
    else:
        return "🟢 baixo"

dados["risco"] = dados["score"].apply(cor)

st.dataframe(dados)

st.map(dados.rename(columns={"lat":"latitude","lon":"longitude"}))
