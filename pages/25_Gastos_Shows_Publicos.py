import streamlit as st
import detector_shows

st.title("🎤 Gastos Públicos com Shows")

df = detector_shows.shows()

st.subheader("📊 Shows pagos com dinheiro público")

st.dataframe(df)

st.subheader("💰 Ranking de gastos")

st.bar_chart(df.set_index("cidade")["valor"])
