import streamlit as st
import inteligencia_central

st.title("🧠 Inteligência Central")

st.write("Painel unificado de risco fiscal, contratos e indícios estatísticos.")

df = inteligencia_central.painel_inteligencia()

st.subheader("🚨 Ranking geral de risco")

st.dataframe(df)

st.subheader("📈 Score total por cidade")

st.bar_chart(df.set_index("cidade")["score_total"])

st.subheader("⚠ Alertas críticos")

criticos = df[df["alerta"] == "🚨 alto risco"]

if criticos.empty:
    st.success("Nenhum município em faixa crítica.")
else:
    st.dataframe(criticos)

st.subheader("🔎 Leitura rápida")

for _, row in df.iterrows():
    st.write(f"{row['cidade']}: {row['alerta']} | score {row['score_total']}")
