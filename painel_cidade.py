import streamlit as st
import painel_idade

st.title("🏙️ Painel Investigativo da Cidade")

codigo = st.text_input("Código IBGE", "3550308")

if st.button("Gerar painel"):

    dados = painel_idade.gerar_painel(codigo)

    st.subheader("📊 Estatísticas")

    st.metric("Total de contratos", dados["total_contratos"])
    st.metric("Orçamento total", f"R$ {dados['valor_total']:,.0f}")

    st.subheader("🏢 Empresas com mais contratos")

    st.dataframe(dados["top_empresas"])

    st.subheader("📋 Contratos encontrados")

    st.dataframe(dados["contratos"])

    if not dados["top_empresas"].empty:

        st.subheader("📈 Distribuição por empresa")

        st.bar_chart(
            dados["top_empresas"].set_index("empresa")["valor"]
        )
