import streamlit as st
import pncp_api

st.title("🏛️ Contratos Públicos Reais")

st.write("Dados do Portal Nacional de Contratações Públicas")

df = pncp_api.buscar_contratos()

if df.empty:

    st.warning("Não foi possível carregar contratos.")

else:

    st.subheader("📋 Contratos recentes")

    st.dataframe(df)

    st.subheader("🏢 Empresas que mais recebem contratos")

    ranking = df.groupby("empresa")["valor"].count().reset_index()

    ranking = ranking.sort_values("valor",ascending=False)

    st.dataframe(ranking)

    st.bar_chart(ranking.set_index("empresa")["valor"])
