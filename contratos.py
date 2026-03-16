import streamlit as st
import pandas as pd
import requests

st.title("🏢 Contratos Públicos Reais")

st.write("Investigação de contratos do Portal Nacional de Contratações Públicas")

def buscar_contratos():

    url = "https://pncp.gov.br/api/consulta/v1/contratos"

    try:

        r = requests.get(url, timeout=30)

        dados = r.json()

        contratos = []

        if isinstance(dados, list):

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

if df.empty:

    st.warning("Nenhum contrato carregado no momento")

else:

    st.subheader("📋 Contratos encontrados")

    st.dataframe(df)

    ranking = df.groupby("empresa")["valor"].sum().reset_index()

    ranking = ranking.sort_values("valor", ascending=False)

    st.subheader("🏢 Empresas que mais recebem")

    st.dataframe(ranking)
