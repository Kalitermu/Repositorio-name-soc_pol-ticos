
import streamlit as st
import pandas as pd
from bloco_risco import calcular_risco, mostrar_painel_risco, mostrar_alertas

st.title("🚨 Radar Transparência Pública")
st.write("Sistema SOC Transparência ativo")

# exemplo de dados para teste
data = {
"_conta_ref":["Conta A","Conta B","Conta C","Conta D"],
"_valor_base":[1000000,2000000,9000000,300000]
}

df = pd.DataFrame(data)

df = calcular_risco(df)

st.subheader("🚨 Alertas de risco")

alertas = df[df["risco"] != "Normal"]

st.dataframe(alertas[["_conta_ref","_valor_base","zscore","risco"]])
