import streamlit as st
import pydeck as pdk
import mapa_nacional

st.title("🌎 Radar Nacional de Risco Fiscal")

df = mapa_nacional.dados_municipios()

def cor(score):

    if score >= 8:
        return [255,0,0]

    elif score >= 6:
        return [255,165,0]

    else:
        return [0,200,0]

df["cor"] = df["score"].apply(cor)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position='[lon, lat]',
    get_color="cor",
    get_radius=70000,
    pickable=True
)

view = pdk.ViewState(
    latitude=-14,
    longitude=-52,
    zoom=3
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view,
    tooltip={"text":"{municipio}\nScore: {score}"}
)

st.pydeck_chart(deck)

st.subheader("📊 Ranking nacional")

st.dataframe(df.sort_values("score",ascending=False))
