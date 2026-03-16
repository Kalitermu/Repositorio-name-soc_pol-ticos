import streamlit as st
import pandas as pd
import requests

st.title("🏢 Contratos Públicos Reais")

st.write("Dados reais do Portal Nacional de Contratações Públicas (PNCP)")

# -----------------------------
# BUSCAR DADOS DO GOVERNO
# -----------------------------

def buscar_contratos():

    url = "https://pncp.gov.br/api/consulta/v1/contratos"

    try:
        r = requests.get(url, timeout=30)

        dados = r.json()

        contratos = []

        for item in dados[:50]:

            cidade = item.get("orgaoEntidade", {}).get("municipioNome")

            obra = item.get("objeto")

            empresa = item.get("fornecedor")

            valor = item.get("valorGlobal")

            contratos.append({
                "cidade": cidade,
                "obra": obra,
                "empresa": empresa,
                "valor": valor
            })

        return pd.DataFrame(contratos)

    except:
        return pd.DataFrame()


df = buscar_contratos()

# -----------------------------
# SE NÃO CARREGAR
# -----------------------------

if df.empty:

    st.error("Não foi possível carregar contratos agora.")

    st.stop()


# -----------------------------
# LISTA
# -----------------------------

st.subheader("📋 Contratos encontrados")

st.dataframe(df)


# -----------------------------
# EMPRESAS QUE MAIS RECEBEM
# -----------------------------

ranking = df.groupby("empresa")["valor"].sum().reset_index()

ranking = ranking.sort_values("valor", ascending=False)

st.subheader("🏢 Empresas que mais recebem")

st.dataframe(ranking)


# -----------------------------
# ALERTA DE VALORES ALTOS
# -----------------------------

media = df["valor"].mean()

df["alerta"] = df["valor"].apply(
    lambda x: "⚠️ valor alto" if x > media*2 else "normal"
)

st.subheader("🚨 Possível valor suspeito")

st.dataframe(df)


# -----------------------------
# GRÁFICO
# -----------------------------

st.subheader("📊 Gastos por empresa")

graf = df.groupby("empresa")["valor"].sum()

st.bar_chart(graf)
