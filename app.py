
import streamlit as st
import pandas as pd
import pydeck as pdk
from bloco_risco import calcular_risco

st.title("🚨 Radar Transparência Pública")

st.write("Auditoria automática de dados públicos")

data = {
"municipio":["São Vicente","Santos","Praia Grande","Guarujá","Cubatão"],
"lat":[-23.96,-23.96,-24.00,-23.99,-23.89],
"lon":[-46.39,-46.33,-46.40,-46.25,-46.42],
"_valor_base":[192000000000,120000000000,80000000000,50000000000,40000000000]
}

df = pd.DataFrame(data)

df = calcular_risco(df.rename(columns={"_valor_base":"_valor_base"}))

st.subheader("📊 Ranking de risco por cidade")

ranking = df.sort_values("_valor_base",ascending=False)

st.dataframe(ranking)

st.bar_chart(ranking.set_index("municipio")["_valor_base"])

st.subheader("🗺️ Mapa de risco fiscal")

layer = pdk.Layer(
"ScatterplotLayer",
data=df,
get_position='[lon, lat]',
get_color='[200, 30, 0, 160]',
get_radius=5000
)

view_state = pdk.ViewState(
latitude=-23.95,
longitude=-46.35,
zoom=8
)

deck = pdk.Deck(layers=[layer], initial_view_state=view_state)

st.pydeck_chart(deck)

st.subheader("🚨 Alertas")

alertas = df[df["risco"]!="Normal"]

st.dataframe(alertas)


import contratos

st.subheader("🏢 Empresas que mais ganham contratos")

ranking_empresas = contratos.empresas_suspeitas()

st.dataframe(ranking_empresas)

st.bar_chart(ranking_empresas.set_index("empresa"))


import detector_corrupcao

st.subheader("🚨 Detector automático de irregularidades")

df_contratos = ranking_empresas.rename(columns={"empresa":"empresa","valor":"valor"})

alertas = detector_corrupcao.detectar_irregularidades(df_contratos)

st.dataframe(alertas)


import pydeck as pdk
import mapa_brasil

st.subheader("🗺 Mapa nacional de risco fiscal")

df_mapa = mapa_brasil.dados_brasil()

layer = pdk.Layer(
"ScatterplotLayer",
data=df_mapa,
get_position='[lon, lat]',
get_color='[200, 30, 0, 160]',
get_radius=60000
)

view_state = pdk.ViewState(
latitude=-14,
longitude=-52,
zoom=3
)

deck = pdk.Deck(layers=[layer], initial_view_state=view_state)

st.pydeck_chart(deck)


import ia_risco

st.subheader("🧠 Previsão de risco com IA")

df_risco = ia_risco.prever_risco(df_contratos)

st.dataframe(df_risco)

st.bar_chart(df_risco.set_index("empresa")["score_risco"])


import programas_sociais

st.subheader("🌎 Comparação com programas sociais")

df_social = programas_sociais.dados_sociais()

st.dataframe(df_social)

st.bar_chart(df_social.set_index("cidade")["beneficiarios"])


import ranking_nacional

st.subheader("🏆 Ranking nacional de risco fiscal")

df_ranking = ranking_nacional.ranking_municipios()

st.dataframe(df_ranking)

st.bar_chart(df_ranking.set_index("municipio")["risco"])


import painel_investigativo

st.subheader("🕵 Painel investigativo")

df_invest = painel_investigativo.painel_investigativo()

st.dataframe(df_invest)

st.bar_chart(df_invest.set_index("municipio")["gasto_publico"])


import detector_anomalias

st.subheader("🚨 Detector de anomalias financeiras")

df_anom = detector_anomalias.detectar_anomalias(df)

anomalias = df_anom[df_anom["alerta"] != "normal"]

st.dataframe(anomalias[["_conta_ref","_valor_base","zscore","alerta"]])


import padroes_municipios

st.subheader("🔎 Padrões suspeitos entre municípios")

df_padrao = padroes_municipios.padroes_municipios()

st.dataframe(df_padrao)

st.bar_chart(df_padrao.set_index("municipio")["gasto_publico"])
