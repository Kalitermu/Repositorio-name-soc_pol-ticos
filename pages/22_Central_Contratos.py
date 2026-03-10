import streamlit as st
import base_contratos
import busca_empresa_contratos

st.title("🏛️ Central de Contratos Públicos")

df = base_contratos.carregar_base()

busca = st.text_input("Buscar empresa", "")

resultado = busca_empresa_contratos.buscar_empresa(busca)

st.subheader("📋 Contratos encontrados")
st.dataframe(resultado)

ranking = busca_empresa_contratos.ranking_empresas()

st.subheader("🏢 Ranking de empresas")
st.dataframe(ranking)

st.subheader("📊 Valor total por empresa")
st.bar_chart(ranking.set_index("empresa")["valor_total"])

st.subheader("📌 Resumo")
st.metric("Total de contratos", len(df))
st.metric("Empresas únicas", df["empresa"].nunique())
st.metric("Valor total", f"R$ {df['valor'].sum():,.0f}")
