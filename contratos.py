import streamlit as st
import pandas as pd
import sys
import os

# garante encontrar módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# tenta importar coletor
try:
    from coletor_obras_pncp import buscar_obras
except:
    def buscar_obras():
        return pd.DataFrame()


st.title("🏢 Contratos Públicos")

st.write("""
Esta página mostra:

• empresas que mais recebem contratos  
• concentração de fornecedores  
• ranking de contratos  
• comparação de valores  
""")


# -----------------------------
# DADOS DE EXEMPLO
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


# -----------------------------
# RANKING
# -----------------------------

st.subheader("📊 Ranking de empresas")

st.dataframe(ranking)


# -----------------------------
# ALERTAS
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

st.subheader("🏗️ Obras públicas")

df_obras = buscar_obras()

# se não vier nada da API
if df_obras.empty:

    st.warning("Nenhuma obra real carregada. Mostrando exemplo.")

    dados_obras = {
        "cidade": [
            "Praia Grande",
            "Santos",
            "São Paulo",
            "Guarulhos",
            "Itanhaém"
        ],

        "obra": [
            "Pavimentação urbana",
            "Construção de escola",
            "Reforma de hospital",
            "Ampliação de terminal",
            "Revitalização da orla"
        ],

        "empresa": [
            "Construtora Alpha",
            "Infra Brasil",
            "Construtora Alpha",
            "Porto Engenharia",
            "Litoral Obras"
        ],

        "valor": [
            120000,
            850000,
            2000000,
            450000,
            700000
        ]
    }

    df_obras = pd.DataFrame(dados_obras)


st.subheader("📋 Lista de obras")

st.dataframe(df_obras)


# -----------------------------
# GRÁFICO POR CIDADE
# -----------------------------

if "cidade" in df_obras.columns:

    st.subheader("📊 Gastos por cidade")

    graf = df_obras.groupby("cidade")["valor"].sum()

    st.bar_chart(graf)
