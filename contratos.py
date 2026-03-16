import streamlit as st
import pandas as pd
import requests

st.title("🏢 Contratos Públicos Reais")
st.write("Dados do Portal Nacional de Contratações Públicas")

def buscar_contratos():

    url = "https://pncp.gov.br/api/consulta/v1/contratos"

    try:
        r = requests.get(url, timeout=30)
        dados = r.json()

        contratos = []

        # PNCP geralmente retorna um dicionário com "data"
        lista = dados.get("data", [])

        for item in lista[:30]:

            cidade = item.get("orgaoEntidade", {}).get("municipioNome", "N/A")

            obra = item.get("objeto", "N/A")

            empresa = item.get("fornecedor", "N/A")

            valor = item.get("valorGlobal", 0)

            contratos.append({
                "cidade": cidade,
                "obra": obra,
                "empresa": empresa,
                "valor": valor
            })

        return pd.DataFrame(contratos)

    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()


df = buscar_contratos()

if df.empty:

    st.warning("Não foi possível carregar contratos agora.")

else:

    st.subheader("📋 Contratos encontrados")
    st.dataframe(df)

    ranking = df.groupby("empresa")["valor"].sum().reset_index()
    ranking = ranking.sort_values("valor", ascending=False)

    st.subheader("🏢 Empresas que mais recebem")
    st.dataframe(ranking)

    st.subheader("📊 Gastos por empresa")
    st.bar_chart(ranking.set_index("empresa"))
