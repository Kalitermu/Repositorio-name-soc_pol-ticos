import streamlit as st
import pandas as pd

st.title("🏢 Contratos Públicos")

st.write("Investigação simples de contratos públicos")


# -----------------------------
# DADOS (exemplo)
# -----------------------------

dados = {
    "cidade": [
        "Praia Grande",
        "Santos",
        "São Paulo",
        "Praia Grande",
        "Guarulhos"
    ],

    "obra": [
        "Pavimentação urbana",
        "Construção de escola",
        "Reforma hospital",
        "Campo futebol",
        "Terminal ônibus"
    ],

    "empresa": [
        "Construtora Alpha",
        "Infra Brasil",
        "Construtora Alpha",
        "Construtora Alpha",
        "Porto Engenharia"
    ],

    "valor": [
        120000,
        850000,
        2000000,
        17000000,
        450000
    ]
}

df = pd.DataFrame(dados)


# -----------------------------
# LISTA DE OBRAS
# -----------------------------

st.subheader("📋 Lista de obras")

st.dataframe(df)


# -----------------------------
# EMPRESAS QUE MAIS GANHAM
# -----------------------------

ranking = df.groupby("empresa")["valor"].sum().reset_index()

ranking = ranking.sort_values("valor", ascending=False)

st.subheader("🏢 Empresas que mais recebem")

st.dataframe(ranking)


# -----------------------------
# ALERTA DE VALOR ALTO
# -----------------------------

media = df["valor"].mean()

df["alerta"] = df["valor"].apply(
    lambda x: "⚠️ valor alto" if x > media*2 else "normal"
)

st.subheader("🚨 Possíveis valores suspeitos")

st.dataframe(df)


# -----------------------------
# GRÁFICO
# -----------------------------

st.subheader("📊 Gastos por empresa")

graf = df.groupby("empresa")["valor"].sum()

st.bar_chart(graf)
