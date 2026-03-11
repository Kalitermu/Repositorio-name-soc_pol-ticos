import streamlit as st
import pandas as pd
import ia_corrupcao
from tesouro_api import buscar_dados_municipio

st.title("🧠 IA de Detecção de Corrupção")

codigo = st.text_input("Código IBGE do município", "3550308")

if st.button("Analisar"):

    df = buscar_dados_municipio(codigo)

    if df is None or df.empty:
        st.warning("Não foi possível carregar dados.")
        st.stop()

    if "valor" in df.columns:
        df["valor_calc"] = pd.to_numeric(df["valor"], errors="coerce")
    elif "valor_item" in df.columns:
        df["valor_calc"] = pd.to_numeric(df["valor_item"], errors="coerce")
    else:
        st.warning("Coluna de valor não encontrada.")
        st.stop()

    analise = ia_corrupcao.analisar(df)

    if analise is None or analise.empty:
        st.success("Nenhuma anomalia detectada.")
        st.stop()

    if "alerta" not in analise.columns:
        analise["alerta"] = "normal"

    st.subheader("🚨 Alertas detectados")

    alertas = analise[analise["alerta"] != "normal"]

    if alertas.empty:
        st.success("Nenhum alerta encontrado.")
    else:
        st.dataframe(alertas)
