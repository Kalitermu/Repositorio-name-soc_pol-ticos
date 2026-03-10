
import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("Benefícios Sociais")

st.write("Análise de famílias, dependentes e valores do Bolsa Família")

data = {
    "cidade":[
        "Praia Grande",
        "Santos",
        "São Vicente",
        "Guarujá"
    ],
    "lat":[
        -24.0058,
        -23.9608,
        -23.9631,
        -23.9933
    ],
    "lon":[
        -46.4028,
        -46.3336,
        -46.3919,
        -46.2564
    ],
    "familias":[
        18000,
        10800,
        15000,
        12000
    ],
    "dependentes":[
        32000,
        19000,
        27000,
        21000
    ],
    "valor_pago":[
        9000000,
        6200000,
        7500000,
        6800000
    ]
}

df = pd.DataFrame(data)

df["media_por_familia"] = df["valor_pago"] / df["familias"]

st.subheader("Tabela de benefícios")

st.dataframe(df)

st.subheader("Valor total pago por cidade")

st.bar_chart(
    df.set_index("cidade")["valor_pago"]
)

st.subheader("Média por família")

st.bar_chart(
    df.set_index("cidade")["media_por_familia"]
)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position="[lon, lat]",
    get_radius="dependentes",
    get_fill_color=[255,120,0,160],
    pickable=True
)

view = pdk.ViewState(
    latitude=-23.97,
    longitude=-46.35,
    zoom=8
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view,
    tooltip={"text":"{cidade}\nFamílias: {familias}\nDependentes: {dependentes}\nValor: {valor_pago}"}
)

st.subheader("Mapa de beneficiários")

st.pydeck_chart(deck)
