import streamlit as st
import pandas as pd
from tesouro_api import buscar_dados_municipio
import ia_corrupcao

st.title("🧠 IA de Detecção de Corrupção")

codigo = st.text_input(
"Código IBGE do município",
"3550308"
)

if st.button("Analisar"):

    df = buscar_dados_municipio(codigo)

    if df.empty:

        st.warning("Não foi possível carregar dados.")

    else:

        if "valor" in df.columns:
            df["valor_calc"] = pd.to_numeric(df["valor"], errors="coerce")

        elif "valor_item" in df.columns:
            df["valor_calc"] = pd.to_numeric(df["valor_item"], errors="coerce")

        df = df.dropna(subset=["valor_calc"])

        analise = ia_corrupcao.analisar_corrupcao(df)

        st.subheader("🚨 Alertas detectados")

        alertas = analise[analise["alerta"] != "normal"]

        st.dataframe(alertas.head(20))

        st.subheader("📊 Ranking de risco")

        st.dataframe(analise.head(20))

        st.bar_chart(analise.set_index("conta")["score_risco"])
