import streamlit as st
import pydeck as pdk
import mapa_sp_interativo

st.title("🗺️ Mapa Interativo de Risco Fiscal")

df = mapa_sp_interativo.dados()

def cor(risco):

    if risco >= 7:
        return [255,0,0]

    elif risco >= 5:
        return [255,165,0]

    else:
        return [0,200,0]

df["cor"] = df["risco"].apply(cor)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position='[lon, lat]',
    get_color='cor',
    get_radius=4000
)

view_state = pdk.ViewState(
    latitude=-23.6,
    longitude=-46.5,
    zoom=8
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state
)

st.pydeck_chart(deck)

st.subheader("📊 Tabela de risco")

st.dataframe(df)
