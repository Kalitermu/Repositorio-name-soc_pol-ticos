import streamlit as st
import pandas as pd
from tesouro_api import buscar_dados_municipio
import investigacao_financeira

st.title("🔎 Modo Investigação")

st.write("""
Ferramentas de análise investigativa de orçamento.

Aqui aparecem:
- contas com crescimento anormal
- valores repetidos
- picos de gasto
- ranking de risco fiscal
""")

df = buscar_dados_municipio("3550308")

if df.empty:

    st.warning("Não foi possível carregar dados do Tesouro.")

else:

    if "valor" in df.columns:
        df["valor_calc"] = pd.to_numeric(df["valor"], errors="coerce")

    elif "valor_item" in df.columns:
        df["valor_calc"] = pd.to_numeric(df["valor_item"], errors="coerce")

    else:
        st.error("Coluna de valor não encontrada.")
        st.stop()

    df = df.dropna(subset=["valor_calc"])

    analise = investigacao_financeira.analisar(df)

    st.subheader("📊 Resultado da investigação")

    st.dataframe(analise.head(20))

    alertas = analise[analise["alerta"] != "normal"]

    st.subheader("🚨 Alertas encontrados")

    st.dataframe(alertas)
