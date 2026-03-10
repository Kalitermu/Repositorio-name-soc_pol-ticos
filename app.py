
import streamlit as st
import pandas as pd
from bloco_risco import calcular_risco

st.title("🚨 Radar Transparência Pública")

st.write("Auditoria automática de dados públicos")

data = {
"municipio":["São Vicente","Santos","Praia Grande","Guarujá","Cubatão"],
"_valor_base":[192000000000,120000000000,80000000000,50000000000,40000000000]
}

df = pd.DataFrame(data)

df = calcular_risco(df.rename(columns={"_valor_base":"_valor_base"}))

st.subheader("📊 Ranking de risco por cidade")

ranking = df.sort_values("_valor_base",ascending=False)

st.dataframe(ranking)

st.bar_chart(ranking.set_index("municipio")["_valor_base"])

st.subheader("🚨 Alertas")

alertas = df[df["risco"]!="Normal"]

st.dataframe(alertas)
