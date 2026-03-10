import streamlit as st
import pydeck as pdk
import scanner_nacional

st.title("🛰️ Scanner Nacional")

st.write("Scanner automático de risco fiscal e contratos por município.")

df = scanner_nacional.executar_scanner()

if df.empty:
    st.warning("Nenhum dado disponível no scanner.")
    st.stop()

st.subheader("🏆 Ranking nacional")
st.dataframe(df)

def cor(alerta: str):
    if "alto" in alerta:
        return [255, 0, 0]
    if "médio" in alerta:
        return [255, 165, 0]
    return [0, 180, 0]

df["cor"] = df["alerta"].apply(cor)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position='[lon, lat]',
    get_fill_color='cor',
    get_radius=50000,
    pickable=True
)

view = pdk.ViewState(latitude=-23.9, longitude=-46.3, zoom=6)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view,
    tooltip={"text": "{cidade}\nScore: {score_total}\nAlerta: {alerta}"}
)

st.subheader("🌎 Mapa de risco")
st.pydeck_chart(deck)

st.subheader("📈 Score total por cidade")
st.bar_chart(df.set_index("cidade")["score_total"])
