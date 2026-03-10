import streamlit as st
import pandas as pd
from tesouro_api import buscar_dados_municipio
import investigacao_financeira
import score_corrupcao

st.title("🔎 Modo Investigação")

cidades = {
    "São Paulo": "3550308",
    "Praia Grande": "3541000",
    "Santos": "3548500"
}

cidade = st.selectbox("Escolha a cidade", list(cidades.keys()))
codigo = cidades[cidade]

df = buscar_dados_municipio(codigo)

if df.empty:

    st.warning("Não foi possível carregar dados.")

else:

    if "valor" in df.columns:
        df["valor_calc"] = pd.to_numeric(df["valor"], errors="coerce")

    elif "valor_item" in df.columns:
        df["valor_calc"] = pd.to_numeric(df["valor_item"], errors="coerce")

    df = df.dropna(subset=["valor_calc"])

    score = score_corrupcao.calcular_score(df)

    st.subheader("🚨 Score de risco fiscal")

    st.metric("Score de corrupção", score)

    analise = investigacao_financeira.analisar(df)

    st.subheader("📊 Análise investigativa")

    st.dataframe(analise.head(20))

    alertas = analise[analise["alerta"] != "normal"]

    st.subheader("🚨 Alertas encontrados")

    st.dataframe(alertas)
