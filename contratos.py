import streamlit as st
import pandas as pd
import requests

st.title("🏢 Contratos Públicos Reais")

st.write("Dados do Portal Nacional de Contratações Públicas")

def buscar_contratos():

    url = "https://pncp.gov.br/api/consulta/v1/contratos"

    r = requests.get(url)

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


df = buscar_contratos()

st.subheader("📋 Contratos encontrados")

st.dataframe(df)

ranking = df.groupby("empresa")["valor"].sum().reset_index()

ranking = ranking.sort_values("valor", ascending=False)

st.subheader("🏢 Empresas que mais recebem")

st.dataframe(ranking)
