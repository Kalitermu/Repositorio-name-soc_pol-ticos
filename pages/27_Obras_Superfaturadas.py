import streamlit as st
import detector_obras_superfaturadas

st.title("🏗️ Detector de Obras Superfaturadas")

df = detector_obras_superfaturadas.analisar()

if df.empty:

    st.success("Nenhuma obra suspeita encontrada")

else:

    st.subheader("🚨 Obras com valor muito acima da média")

    st.dataframe(df)

    st.bar_chart(df.set_index("cidade")["valor"])
