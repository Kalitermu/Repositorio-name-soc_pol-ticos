import streamlit as st
import pandas as pd
import random

st.title("🚨 Radar Fiscal")

st.write("Análise estatística de gastos públicos.")

# Dados simulados (até conectar API real)

dados = pd.DataFrame({
    "conta": ["Saúde", "Educação", "Infraestrutura", "Segurança", "Assistência Social"],
    "valor": [
        random.randint(10000000, 80000000),
        random.randint(10000000, 80000000),
        random.randint(10000000, 80000000),
        random.randint(10000000, 80000000),
        random.randint(10000000, 80000000)
    ]
})

total = dados["valor"].sum()
media = dados["valor"].mean()
desvio = dados["valor"].std()

st.subheader("📊 Estatísticas")

st.metric("Somatório do orçamento", f"R$ {total:,.0f}")
st.metric("Média de gastos", f"R$ {media:,.0f}")
st.metric("Desvio padrão", f"R$ {desvio:,.0f}")

st.subheader("📋 Principais contas")

st.dataframe(dados)

st.subheader("📈 Distribuição de despesas")

st.bar_chart(dados.set_index("conta"))
