import streamlit as st
import pydeck as pdk
from modules.radar_nacional import gerar_base_nacional

st.title("🗺️ Mapa Nacional de Risco Fiscal")

df = gerar_base_nacional()

def cor(score):
    if score >= 7:
        return [220, 30, 30, 160]
    elif score >= 4:
        return [255, 180, 0, 160]
    return [0, 180, 0, 160]

df["color"] = df["score_risco"].apply(cor)
df["raio"] = (df["score_risco"] * 8000).astype(int)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position="[lon, lat]",
    get_radius="raio",
    get_fill_color="color",
    pickable=True
)

view_state = pdk.ViewState(
    latitude=-15.8,
    longitude=-47.9,
    zoom=3.3
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={
        "text": "Cidade: {cidade}\nEstado: {estado}\nScore: {score_risco}\nGasto: {gasto_total}"
    }
)

st.pydeck_chart(deck)
