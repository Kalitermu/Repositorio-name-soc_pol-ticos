import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("🌎 Mapa de Risco Fiscal")

dados = pd.DataFrame({
    "cidade":[
        "São Vicente",
        "Praia Grande",
        "Santos",
        "Guarujá",
        "Cubatão"
    ],
    "lat":[
        -23.96,
        -24.00,
        -23.95,
        -23.99,
        -23.89
    ],
    "lon":[
        -46.38,
        -46.41,
        -46.33,
        -46.25,
        -46.42
    ],
    "score":[
        6.7,
        5.9,
        4.1,
        7.4,
        3.8
    ]
})

def cor(score):
    if score >= 7:
        return [255,0,0]
    elif score >= 4:
        return [255,165,0]
    else:
        return [0,200,0]

dados["cor"] = dados["score"].apply(cor)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=dados,
    get_position='[lon, lat]',
    get_color="cor",
    get_radius=50000,
    pickable=True
)

view = pdk.ViewState(
    latitude=-23.95,
    longitude=-46.35,
    zoom=7
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view,
    tooltip={"text": "{cidade}\nScore de risco: {score}"}
)

st.pydeck_chart(deck)

st.subheader("📊 Ranking de risco fiscal")

st.dataframe(dados.sort_values("score",ascending=False))
