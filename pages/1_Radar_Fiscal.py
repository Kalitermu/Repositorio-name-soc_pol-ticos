import streamlit as st
import pandas as pd
from tesouro_api import buscar_dados_municipio

st.title("🚨 Radar Fiscal")

cidade = st.selectbox(
    "Escolha o município",
    {
        "São Paulo": "3550308",
        "Praia Grande": "3541000",
        "Santos": "3548500"
    }
)

df = buscar_dados_municipio(cidade)

if df.empty:
    st.warning("Não foi possível carregar dados do Tesouro Nacional.")
else:

    valores = pd.to_numeric(df["valor"], errors="coerce").dropna()

    total = valores.sum()
    media = valores.mean()
    desvio = valores.std()

    st.subheader("📊 Estatísticas")

    st.metric("Somatório do orçamento", f"R$ {total:,.0f}")
    st.metric("Média de gastos", f"R$ {media:,.0f}")
    st.metric("Desvio padrão", f"R$ {desvio:,.0f}")

    top = df.sort_values("valor", ascending=False).head(10)

    st.subheader("📋 Principais contas")
    st.dataframe(top)

    st.subheader("📈 Distribuição de despesas")
    st.bar_chart(top.set_index("conta")["valor"])
