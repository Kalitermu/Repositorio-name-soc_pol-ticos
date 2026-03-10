import streamlit as st
import pandas as pd
from tesouro_api import buscar_dados_municipio

st.title("🚨 Radar Fiscal")

cidades = {
    "São Paulo": "3550308",
    "Praia Grande": "3541000",
    "Santos": "3548500"
}

cidade_nome = st.selectbox("Escolha o município", list(cidades.keys()))
codigo = cidades[cidade_nome]

df = buscar_dados_municipio(codigo)

if df.empty:
    st.warning("Não foi possível carregar dados do Tesouro Nacional.")
else:

    # detectar coluna de valor automaticamente
    if "valor" in df.columns:
        valores = pd.to_numeric(df["valor"], errors="coerce")
    elif "valor_item" in df.columns:
        valores = pd.to_numeric(df["valor_item"], errors="coerce")
    else:
        st.error("Coluna de valor não encontrada na API.")
        st.write(df.columns)
        st.stop()

    valores = valores.dropna()

    total = valores.sum()
    media = valores.mean()
    desvio = valores.std()

    st.subheader("📊 Estatísticas")

    st.metric("Somatório do orçamento", f"R$ {total:,.0f}")
    st.metric("Média de gastos", f"R$ {media:,.0f}")
    st.metric("Desvio padrão", f"R$ {desvio:,.0f}")

    df["valor_calc"] = valores

    top = df.sort_values("valor_calc", ascending=False).head(10)

    st.subheader("📋 Principais contas")
    st.dataframe(top)

    st.subheader("📈 Distribuição de despesas")
    st.bar_chart(top["valor_calc"])
