import streamlit as st
import detector_alertas_contratos

st.title("🚨 Alertas de Contratos Públicos")

st.write("Detecção automática de padrões suspeitos.")

df = detector_alertas_contratos.detectar_alertas()

if df.empty:

    st.success("Nenhum alerta detectado.")

else:

    st.subheader("⚠️ Alertas encontrados")

    st.dataframe(df)

    st.bar_chart(df.groupby("empresa")["valor"].sum())
