import streamlit as st
import pandas as pd

# -----------------------------
# TÍTULO
# -----------------------------
st.title("🏢 Contratos Públicos")
st.write("Investigação simples de contratos públicos")

# -----------------------------
# DADOS (exemplo simples)
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
        "Campo de futebol",
        "Terminal de ônibus"
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
# EMPRESAS QUE MAIS RECEBEM
# -----------------------------
ranking = df.groupby("empresa")["valor"].sum().reset_index()
ranking = ranking.sort_values("valor", ascending=False)

st.subheader("🏢 Empresas que mais recebem")
st.dataframe(ranking)

# -----------------------------
# DETECTOR SIMPLES
# -----------------------------
media = df["valor"].mean()

df["alerta"] = df["valor"].apply(
    lambda x: "⚠️ valor alto" if x > media * 2 else "normal"
)

st.subheader("🚨 Possíveis valores suspeitos")
st.dataframe(df)

# -----------------------------
# GRÁFICO
# -----------------------------
st.subheader("📊 Gastos por empresa")
graf = df.groupby("empresa")["valor"].sum()
st.bar_chart(graf)

# -----------------------------
# FILTRO POR CIDADE
# -----------------------------
st.subheader("🔎 Filtrar por cidade")

cidade = st.selectbox(
    "Selecione a cidade",
    ["Todas"] + sorted(df["cidade"].unique().tolist())
)

if cidade != "Todas":
    df_filtrado = df[df["cidade"] == cidade]
else:
    df_filtrado = df

st.dataframe(df_filtrado)
