import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from coletor_obras_pncp import buscar_obras


st.title("🏢 Contratos Públicos")

st.write("Análise de contratos e obras públicas.")

st.write("""
Esta página mostra:

• ranking de empresas  
• detector de irregularidades  
• distribuição de contratos  
• lista de obras públicas
""")


# -----------------------------
# RANKING DE EXEMPLO
# -----------------------------

dados = {
    "empresa": [
        "Construtora Alpha",
        "Construtora Beta",
        "Engenharia Brasil",
        "Infra Litoral",
        "Construtora Alpha",
        "Infra Litoral"
    ],

    "valor_total": [
        5000000,
        7000000,
        3000000,
        2500000,
        8000000,
        4000000
    ]
}

df = pd.DataFrame(dados)

ranking = df.groupby("empresa")["valor_total"].sum().reset_index()

ranking = ranking.sort_values("valor_total", ascending=False)

st.subheader("📊 Ranking de empresas")

st.dataframe(ranking)


# -----------------------------
# DETECTOR
# -----------------------------

ranking["alerta"] = ranking["valor_total"].apply(
    lambda x: "⚠️ atenção" if x > 10000000 else "normal"
)

st.subheader("🚨 Detector de irregularidades")

st.dataframe(ranking)


# -----------------------------
# GRÁFICO
# -----------------------------

st.subheader("📈 Distribuição de contratos")

st.bar_chart(ranking.set_index("empresa")["valor_total"])


# -----------------------------
# OBRAS REAIS
# -----------------------------

st.subheader("🏗️ Obras públicas encontradas")

df_obras = buscar_obras()

st.write("Total de contratos encontrados:", len(df_obras))


# filtro de cidade

cidade = st.selectbox(
    "Filtrar por cidade",
    ["Todas"] + sorted(df_obras["cidade"].dropna().unique().tolist())
)

if cidade != "Todas":
    df_obras = df_obras[df_obras["cidade"] == cidade]


st.dataframe(df_obras)


# gráfico por cidade

if len(df_obras) > 0:

    st.subheader("📊 Valor total por cidade")

    graf = df_obras.groupby("cidade")["valor"].sum()

    st.bar_chart(graf)
