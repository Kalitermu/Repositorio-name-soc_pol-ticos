import streamlit as st
import pncp_api
import grafo_contratos_publicos

st.title("🔗 Rede de Contratos Públicos")

st.write("""
Visualização de conexões entre órgãos públicos e empresas.
""")

df = pncp_api.buscar_contratos()

if df.empty:

    st.warning("Não foi possível carregar contratos.")

else:

    conexoes = grafo_contratos_publicos.gerar_grafo(df)

    st.subheader("📋 Conexões detectadas")

    st.dataframe(conexoes)

    st.subheader("🏢 Empresas mais conectadas")

    ranking = conexoes.groupby("destino")["valor"].count().reset_index()

    ranking = ranking.sort_values("valor",ascending=False)

    st.dataframe(ranking)

    st.bar_chart(ranking.set_index("destino")["valor"])
