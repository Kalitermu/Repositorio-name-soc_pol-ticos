import streamlit as st
import pandas as pd
import pydeck as pdk
import scanner_nacional

st.title("🛰️ Scanner Nacional")
st.write("Scanner automático de risco fiscal e contratos por município.")

try:
    df = scanner_nacional.coletar()
except:
    df = pd.DataFrame()

if df is None:
    df = pd.DataFrame()

if df.empty:
    st.warning("Nenhum dado disponível no scanner.")
    st.stop()

# garantir colunas
if "cidade" not in df.columns:
    df["cidade"] = "desconhecida"

if "alerta" not in df.columns:
    df["alerta"] = "baixo"

if "lat" not in df.columns:
    df["lat"] = -23.9

if "lon" not in df.columns:
    df["lon"] = -46.3

if "score_total" not in df.columns:
    df["score_total"] = 1

st.subheader("🏆 Ranking nacional")
st.dataframe(df)

def cor(alerta):
    if "alto" in str(alerta):
        return [255,0,0]
    if "médio" in str(alerta):
        return [255,165,0]
    return [0,180,0]

df["cor"] = df["alerta"].apply(cor)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position='[lon, lat]',
    get_fill_color='cor',
    get_radius=4000,
)

view = pdk.ViewState(latitude=-23.9, longitude=-46.3, zoom=6)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view,
)

st.subheader("🌎 Mapa de risco")
st.pydeck_chart(deck)

st.subheader("📈 Score total por cidade")
st.bar_chart(df.set_index("cidade")["score_total"])
