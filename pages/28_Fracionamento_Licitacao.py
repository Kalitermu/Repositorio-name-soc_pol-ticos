import streamlit as st
import detector_fracionamento

st.title("🔎 Detector de Fracionamento de Licitação")

df = detector_fracionamento.analisar()

if df.empty:

    st.success("Nenhum fracionamento suspeito detectado")

else:

    st.subheader("🚨 Possível fracionamento de contratos")

    st.dataframe(df)

    st.bar_chart(df.set_index("empresa")["qtd_contratos"])
