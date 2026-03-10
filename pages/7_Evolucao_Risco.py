import streamlit as st
import pandas as pd
import alerta_risco

st.title("📈 Evolução do Risco Fiscal")

dados = pd.DataFrame({
    "ano":[2021,2022,2023,2024],
    "score":[4.2,5.1,5.9,6.7]
})

st.line_chart(dados.set_index("ano"))

mensagem = alerta_risco.alerta_risco(dados)

if mensagem:
    st.write(mensagem)
