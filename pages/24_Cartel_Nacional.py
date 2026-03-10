import streamlit as st
import detector_cartel_nacional

st.title("🚨 Detector Nacional de Cartel de Empresas")

st.write("Análise automática de empresas com contratos em vários órgãos e alta concentração de valor.")

df = detector_cartel_nacional.detectar()

if df.empty:
    st.warning("Nenhum dado de contratos disponível.")
else:
    st.subheader("📊 Empresas analisadas")
    st.dataframe(df)

    suspeitas = df[df["alerta"] != "normal"]

    st.subheader("⚠️ Suspeitas principais")
    if suspeitas.empty:
        st.success("Nenhuma empresa em faixa de atenção.")
    else:
        st.dataframe(suspeitas)

    st.subheader("💰 Valor total por empresa")
    st.bar_chart(df.set_index("empresa")["valor_total"])
