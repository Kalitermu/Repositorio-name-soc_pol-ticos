import streamlit as st
import pandas as pd
import sys
import os

# garante que o Python encontre os módulos do projeto
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from coletor_obras_pncp import buscar_obras
except:
    # caso o módulo não seja encontrado, cria dataframe vazio
    def buscar_obras():
        return pd.DataFrame(columns=["cidade","descricao","empresa","valor_total"])


def empresas_suspeitas():

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

    classificacao = (
        df.groupby("empresa")["valor_total"]
        .sum()
        .reset_index()
    )

    classificacao = classificacao.sort_values(
        "valor_total",
        ascending=False
    )

    return classificacao


# -----------------------------
# TÍTULO
# -----------------------------

st.title("🏢 Contratos Públicos")

st.write("Análise de contratos e empresas.")

st.write("""
Esta página mostra:

• empresas que mais recebem contratos  
• concentração de fornecedores  
• ranking de contratos  
• comparação de valores  
""")


# -----------------------------
# RANKING
# -----------------------------

ranking = empresas_suspeitas()

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
# OBRAS REAIS PNCP
# -----------------------------

st.subheader("🏗️ Obras públicas encontradas")

df_obras = buscar_obras()

if df_obras.empty:
    st.info("Nenhuma obra encontrada ou erro ao carregar dados.")
else:
    st.dataframe(df_obras[[
        "cidade",
        "descricao",
        "empresa",
        "valor_total"
    ]])
