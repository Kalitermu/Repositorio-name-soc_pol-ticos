import streamlit as st
import pandas as pd
import requests

st.title("👨‍👩‍👧 Benefícios Sociais")

st.write("Análise de distribuição de benefícios sociais.")

url = "https://api.portaldatransparencia.gov.br/api-de-dados/bolsa-familia-disponivel-por-municipio"

headers = {
    "chave-api-dados": "SUA_CHAVE_API"
}

params = {
    "mesAno": "202401",
    "codigoIbge": "3541000"
}

try:
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        dados = pd.DataFrame(response.json())

        if not dados.empty:

            st.subheader("Tabela de benefícios")

            st.dataframe(dados)

            if "valor" in dados.columns:
                st.subheader("Distribuição de valores")
                st.bar_chart(dados["valor"])

        else:
            st.warning("Nenhum dado encontrado para o município.")

    else:
        st.error("Erro ao acessar API da transparência.")

except Exception as e:
    st.error("Erro ao carregar dados")
    st.write(e)

