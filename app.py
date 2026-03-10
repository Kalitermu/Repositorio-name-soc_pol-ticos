
import streamlit as st
import pandas as pd
import pydeck as pdk
from bloco_risco import calcular_risco

st.title("🚨 Radar Transparência Pública")

st.write("Auditoria automática de dados públicos")

data = {
"municipio":["São Vicente","Santos","Praia Grande","Guarujá","Cubatão"],
"lat":[-23.96,-23.96,-24.00,-23.99,-23.89],
"lon":[-46.39,-46.33,-46.40,-46.25,-46.42],
"_valor_base":[192000000000,120000000000,80000000000,50000000000,40000000000]
}

df = pd.DataFrame(data)

df = calcular_risco(df.rename(columns={"_valor_base":"_valor_base"}))

st.subheader("📊 Ranking de risco por cidade")

ranking = df.sort_values("_valor_base",ascending=False)

st.dataframe(ranking)

st.bar_chart(ranking.set_index("municipio")["_valor_base"])

st.subheader("🗺️ Mapa de risco fiscal")

layer = pdk.Layer(
"ScatterplotLayer",
data=df,
get_position='[lon, lat]',
get_color='[200, 30, 0, 160]',
get_radius=5000
)

view_state = pdk.ViewState(
latitude=-23.95,
longitude=-46.35,
zoom=8
)

deck = pdk.Deck(layers=[layer], initial_view_state=view_state)

st.pydeck_chart(deck)

st.subheader("🚨 Alertas")

alertas = df[df["risco"]!="Normal"]

st.dataframe(alertas)
