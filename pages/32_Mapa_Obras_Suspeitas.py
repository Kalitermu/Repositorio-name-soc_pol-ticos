import streamlit as st
import pydeck as pdk
import obras_publicas

st.title("🏗️ Mapa de Obras Públicas")

df = obras_publicas.dados()

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position='[lon, lat]',
    get_color='[255,0,0]',
    get_radius=5000,
    pickable=True
)

view = pdk.ViewState(
    latitude=-23.7,
    longitude=-46.4,
    zoom=8
)

tooltip = {
    "html": "<b>Cidade:</b> {cidade}<br>"
            "<b>Obra:</b> {obra}<br>"
            "<b>Empresa:</b> {empresa}<br>"
            "<b>Valor:</b> R$ {valor}",
    "style": {"backgroundColor": "black", "color": "white"}
}

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view,
    tooltip=tooltip
)

st.pydeck_chart(deck)

st.subheader("📊 Lista de obras")

st.dataframe(df)
