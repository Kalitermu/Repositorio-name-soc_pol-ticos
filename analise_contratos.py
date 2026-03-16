import streamlit as st
import pandas as pd

st.title("🏗️ Análise de Obras Públicas")

# Exemplo de dados da obra
obra = {
    "cidade": "Itaquaquecetuba",
    "obra": "Campo de futebol bairro X",
    "valor_oficial": 2700000,
    "area_m2": 7000
}

# custo médio aproximado por m² (exemplo)
custo_medio_m2 = 300

# estimativa IA
valor_estimado = obra["area_m2"] * custo_medio_m2

# faixa estimada
faixa_min = valor_estimado * 0.8
faixa_max = valor_estimado * 1.2

st.subheader("📍 Obra analisada")

st.write(f"Cidade: {obra['cidade']}")
st.write(f"Obra: {obra['obra']}")

st.subheader("💰 Comparação de valores")

col1, col2 = st.columns(2)

with col1:
    st.metric("Valor oficial (prefeitura)", f"R$ {obra['valor_oficial']:,.0f}")

with col2:
    st.metric("Estimativa IA", f"R$ {valor_estimado:,.0f}")

st.subheader("📊 Faixa de referência")

st.write(f"Entre R$ {faixa_min:,.0f} e R$ {faixa_max:,.0f}")

# análise
if obra["valor_oficial"] > faixa_max:
    st.error("🚨 Valor acima da média estimada")
elif obra["valor_oficial"] < faixa_min:
    st.warning("⚠️ Valor abaixo da média estimada")
else:
    st.success("✅ Valor dentro da média estimada")

st.caption("Estimativa baseada em custos médios de obras semelhantes.")
