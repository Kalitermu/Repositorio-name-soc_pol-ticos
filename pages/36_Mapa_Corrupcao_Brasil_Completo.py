import streamlit as st
import pydeck as pdk
import mapa_corrupcao_brasil_completo

st.title("🛰️ Mapa Nacional de Risco de Corrupção")

df = mapa_corrupcao_brasil_completo.gerar_dados()

def cor(alerta):
    if alerta == "alto":
        return [255,0,0]
    if alerta == "medio":
        return [255,165,0]
    return [0,200,0]

df["cor"] = df["alerta"].apply(cor)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position='[lon, lat]',
    get_fill_color='cor',
    get_radius=80000,
    pickable=True
)

view = pdk.ViewState(
    latitude=-15.78,
    longitude=-47.92,
    zoom=4
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view,
    tooltip={"text": "{cidade}\nScore: {score}\nAlerta: {alerta}"}
)

st.pydeck_chart(deck)

st.subheader("📊 Ranking de risco")
st.dataframe(df.sort_values("score", ascending=False))
