import streamlit as st
import detector_desvios
import pandas as pd

st.title("🔎 Investigação de Gastos Públicos")

# exemplo de dados simulados
df = pd.DataFrame({
"cidade":["São Paulo","Guarulhos","Santos","Praia Grande","Suzano"],
"contrato":[
"obra avenida",
"show municipal",
"festival cultural",
"obra pavimentacao",
"evento cidade"
],
"valor":[
5000000,
1200000,
900000,
8000000,
600000
]
})

st.subheader("📊 Contratos analisados")

st.dataframe(df)

suspeitos = detector_desvios.analisar(df)

st.subheader("🚨 Possíveis anomalias")

if suspeitos.empty:
    st.success("Nenhum gasto suspeito detectado")
else:
    st.dataframe(suspeitos)

st.subheader("💰 Comparação de gastos")

st.bar_chart(df.set_index("cidade")["valor"])
