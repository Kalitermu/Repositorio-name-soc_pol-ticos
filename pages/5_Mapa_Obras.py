import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("🗺️ Mapa de Obras Públicas")

st.write("Visualização de investimentos públicos no mapa.")

dados = pd.DataFrame({
    "obra":[
        "Reforma escola municipal",
        "Construção UBS",
        "Pavimentação avenida",
        "Ampliação hospital"
    ],
    "empresa":[
        "Construtora Alpha",
        "Engenharia Brasil",
        "Infra Litoral",
        "Construtora Beta"
    ],
    "valor":[
        4000000,
        7000000,
        3500000,
        12000000
    ],
    "lat":[
        -23.96,
        -24.00,
        -23.95,
        -23.99
    ],
    "lon":[
        -46.38,
        -46.41,
        -46.33,
        -46.25
    ]
})

layer = pdk.Layer(
    "ScatterplotLayer",
    data=dados,
    get_position='[lon, lat]',
    get_radius=50000,
    get_color='[0, 150, 255]',
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
    tooltip={"text": "{obra}\nEmpresa: {empresa}\nValor: R$ {valor}"}
)

st.pydeck_chart(deck)

st.subheader("📊 Lista de obras")

st.dataframe(dados)
