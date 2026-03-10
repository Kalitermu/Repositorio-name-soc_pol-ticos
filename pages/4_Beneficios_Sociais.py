
import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("Benefícios Sociais")

st.write("Análise do Bolsa Família")

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

st.bar_chart(df.set_index("cidade")["valor_pago"])

st.subheader("Média por família")

st.bar_chart(df.set_index("cidade")["media_por_familia"])

# evolução anual

dados_ano = {
    "ano":[2021,2022,2023,2024],
    "valor_pago":[5000000,6800000,8100000,9000000]
}

df_ano = pd.DataFrame(dados_ano)

st.subheader("Evolução do Bolsa Família por ano")

st.line_chart(df_ano.set_index("ano"))

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


import detector_bolsa_familia

st.subheader("🚨 Detector de crescimento do Bolsa Família")

df_alerta = detector_bolsa_familia.detectar_crescimento(df_ano)

st.dataframe(df_alerta)

alertas = df_alerta[df_alerta["alerta"] != "normal"]

if not alertas.empty:
    st.warning("Crescimento anormal detectado")
