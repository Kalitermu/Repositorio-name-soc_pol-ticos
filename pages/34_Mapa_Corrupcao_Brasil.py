import streamlit as st
import pydeck as pdk
import mapa_corrupcao_brasil

st.title("🗺️ Mapa Nacional de Risco de Corrupção")

df = mapa_corrupcao_brasil.dados()

def cor(r):

    if r >= 8:
        return [255,0,0]

    elif r >= 6:
        return [255,165,0]

    else:
        return [0,200,0]

df["cor"] = df["risco"].apply(cor)

layer = pdk.Layer(
"ScatterplotLayer",
data=df,
get_position='[lon, lat]',
get_color='cor',
get_radius=20000
)

view = pdk.ViewState(
latitude=-23.7,
longitude=-46.5,
zoom=6
)

deck = pdk.Deck(
layers=[layer],
initial_view_state=view
)

st.pydeck_chart(deck)

st.subheader("📊 Ranking de risco")

st.dataframe(df.sort_values("risco",ascending=False))
