import streamlit as st
import contratos

st.title("🏢 Contratos Públicos")

df = contratos.buscar_contratos()

if df.empty:

    st.warning("⚠️ Não foi possível carregar contratos.")

else:

    st.subheader("📋 Lista de contratos")
    st.dataframe(df)

    ranking = df.groupby("empresa")["valor"].sum().reset_index()
    ranking = ranking.sort_values("valor", ascending=False)

    st.subheader("🏢 Empresas que mais recebem")
    st.dataframe(ranking)

    st.subheader("📊 Gastos por empresa")
    st.bar_chart(ranking.set_index("empresa"))
