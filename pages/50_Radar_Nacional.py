import streamlit as st
import radar_nacional

st.title("🌎 Radar Nacional de Corrupção")

df = radar_nacional.ranking()

st.subheader("Ranking nacional de risco fiscal")

st.dataframe(df)

st.bar_chart(df.set_index("cidade")["risco"])
