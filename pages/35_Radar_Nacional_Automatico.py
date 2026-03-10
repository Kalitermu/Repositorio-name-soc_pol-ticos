import streamlit as st
import scanner_nacional

st.title("🛰 Radar Nacional Automático de Corrupção")

if st.button("Escanear cidades"):

    df = scanner_nacional.coletar()

    if df.empty:

        st.warning("Nenhum dado encontrado")

    else:

        st.subheader("📊 Ranking de risco")

        st.dataframe(df.sort_values("risco",ascending=False))

        st.bar_chart(df.set_index("cidade")["risco"])
