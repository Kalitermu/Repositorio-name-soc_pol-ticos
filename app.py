
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


import grafo_contratos
import streamlit.components.v1 as components

st.subheader("🔗 Rede de contratos entre municípios e empresas")

arquivo = grafo_contratos.gerar_grafo()

with open(arquivo,"r",encoding="utf-8") as f:
    components.html(f.read(), height=520)


import redes_suspeitas

st.subheader("🧠 Detector de redes suspeitas de contratos")

df_redes = redes_suspeitas.detectar_redes_suspeitas()

st.dataframe(df_redes)

st.bar_chart(df_redes.set_index("empresa")["score_centralidade"])


import distribuicao_dinheiro

st.subheader("💰 Distribuição do dinheiro público")

df_dist = distribuicao_dinheiro.distribuicao_dinheiro()

st.dataframe(df_dist)

st.bar_chart(df_dist.set_index("categoria")["valor"])


st.subheader("🥧 Distribuição percentual do orçamento")

st.write(df_dist[["categoria","percentual"]])

st.bar_chart(df_dist.set_index("categoria")["percentual"])


import indice_social

st.subheader("🌎 Índice social por município")

df_social = indice_social.indice_social()

st.dataframe(df_social)

st.bar_chart(df_social.set_index("cidade")["indice_social"])


import pydeck as pdk
import dados_integrados

st.subheader("🗺️ Mapa integrado de gasto, contratos e benefícios sociais")

df_mapa_integrado = dados_integrados.dados_integrados()

st.dataframe(df_mapa_integrado[[
    "municipio",
    "gasto_publico",
    "contratos",
    "beneficios_sociais",
    "indice_social",
    "score_integrado"
]])

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df_mapa_integrado,
    get_position="[lon, lat]",
    get_radius="raio",
    get_fill_color="[200, 30, 0, 140]",
    pickable=True
)

view_state = pdk.ViewState(
    latitude=-23.96,
    longitude=-46.36,
    zoom=8
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={
        "text": "Município: {municipio}\nGasto: {gasto_publico}\nContratos: {contratos}\nBenefícios: {beneficios_sociais}\nÍndice social: {indice_social}\nScore integrado: {score_integrado}"
    }
)

st.pydeck_chart(deck)

st.subheader("📊 Score integrado por município")
st.bar_chart(df_mapa_integrado.set_index("municipio")["score_integrado"])


import grafo_dinheiro
import streamlit.components.v1 as components

st.subheader("🔗 Grafo de conexões do dinheiro público")

arquivo = grafo_dinheiro.grafo_completo()

with open(arquivo,"r",encoding="utf-8") as f:
    components.html(f.read(),height=620)


import investimentos_areas

st.subheader("💰 Investimento por área pública")

df_area = investimentos_areas.investimentos_areas()

st.dataframe(df_area)

st.subheader("📊 Comparação por área")

st.bar_chart(
    df_area.set_index("municipio")[[
        "saude",
        "educacao",
        "obras",
        "seguranca",
        "social"
    ]]
)


import alertas_areas

st.subheader("🚨 Alertas de distribuição de investimento")

alertas = alertas_areas.alertas_areas(df_area)

for a in alertas:
    st.warning(a)


import pydeck as pdk
import mapa_investimentos

st.subheader("🗺️ Mapa de investimento público por área")

df_mapa = mapa_investimentos.mapa_investimentos()

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df_mapa,
    get_position="[lon, lat]",
    get_radius="raio",
    get_fill_color="[0, 150, 255, 140]",
    pickable=True
)

view_state = pdk.ViewState(
    latitude=-23.96,
    longitude=-46.36,
    zoom=8
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={
        "text": "Município: {municipio}\nSaúde: {saude}\nEducação: {educacao}\nObras: {obras}"
    }
)

st.pydeck_chart(deck)


import ranking_eficiencia

st.subheader("🏆 Ranking de eficiência pública")

df_rank = ranking_eficiencia.ranking_eficiencia()

st.dataframe(df_rank[[
    "municipio",
    "indice_eficiencia"
]])

st.bar_chart(
    df_rank.set_index("municipio")["indice_eficiencia"]
)


import evolucao_gastos
import anomalia_orcamento

st.subheader("📈 Evolução do orçamento público")

df_hist = evolucao_gastos.evolucao_gastos()

st.dataframe(df_hist)

st.line_chart(df_hist.set_index("ano"))

st.subheader("🚨 Detector de crescimento anormal")

alertas = anomalia_orcamento.detectar_anomalia(df_hist)

for a in alertas:
    st.warning(a)


import previsao_gastos

st.subheader("🔮 Previsão de gasto público")

df_prev = previsao_gastos.prever_gastos()

st.dataframe(df_prev)

st.bar_chart(df_prev.set_index("cidade")["previsao_2024"])


import risco_fiscal

st.subheader("⚠ Indicador de risco fiscal futuro")

df_risco = risco_fiscal.risco_fiscal()

st.dataframe(df_risco)

st.bar_chart(
    df_risco.set_index("cidade")["crescimento"]
)


import indice_transparencia

st.subheader("🏛 Índice de transparência municipal")

df_transp = indice_transparencia.indice_transparencia()

st.dataframe(df_transp)

st.bar_chart(
    df_transp.set_index("cidade")["score_transparencia"]
)


import pydeck as pdk
import mapa_transparencia

st.subheader("🗺️ Mapa de transparência municipal")

df_map_transp = mapa_transparencia.mapa_transparencia()

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df_map_transp,
    get_position="[lon, lat]",
    get_radius="raio",
    get_fill_color="color",
    pickable=True
)

view_state = pdk.ViewState(
    latitude=-23.96,
    longitude=-46.36,
    zoom=8
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={
        "text": "Cidade: {cidade}\nScore: {score}"
    }
)

st.pydeck_chart(deck)


import api_transparencia

st.subheader("🌐 Dados reais do Portal da Transparência")

api_key = st.text_input("Digite sua chave da API")

if api_key:

    df_api = api_transparencia.dados_transparencia(api_key)

    st.dataframe(df_api)


import pncp_api
import tesouro_api

st.subheader("🏢 Contratos públicos (PNCP)")

df_contratos = pncp_api.contratos_pncp()

st.dataframe(df_contratos)

st.subheader("💰 Dados fiscais (Tesouro Nacional)")

df_tesouro = tesouro_api.dados_tesouro()

st.dataframe(df_tesouro)


import radar_corrupcao

st.subheader("🚨 Radar automático de risco de contratos")

if "df_contratos" in locals():

    df_risco = radar_corrupcao.radar_corrupcao(df_contratos)

    st.dataframe(df_risco)

    if not df_risco.empty:
        st.bar_chart(df_risco["valor"])


import empresas_multicidades

st.subheader("🏢 Empresas com contratos em várias cidades")

df_empresas_map, df_empresas_rank = empresas_multicidades.empresas_multicidades()

st.write("Ranking de empresas por número de cidades")

st.dataframe(df_empresas_rank)

st.bar_chart(
    df_empresas_rank.set_index("empresa")["cidades"]
)


import repeticao_contratos

st.subheader("🔁 Empresas com contratos repetidos no mesmo órgão")

df_rep = repeticao_contratos.repeticao_por_orgao()

st.dataframe(df_rep)

st.bar_chart(df_rep.set_index("empresa")["contratos"])


import fracionamento_contratos

st.subheader("💰 Detector de possíveis fracionamentos de contratos")

df_valores, df_grupos = fracionamento_contratos.detectar_valores_parecidos()

st.write("Valores analisados")

st.dataframe(df_valores)

st.write("Grupos de valores próximos")

st.dataframe(df_grupos)


import pydeck as pdk
import mapa_contratos_suspeitos

st.subheader("🗺️ Mapa de contratos suspeitos")

df_map = mapa_contratos_suspeitos.contratos_suspeitos()

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df_map,
    get_position="[lon, lat]",
    get_radius="raio",
    get_fill_color="color",
    pickable=True
)

view_state = pdk.ViewState(
    latitude=-23.96,
    longitude=-46.36,
    zoom=8
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={
        "text": "Cidade: {cidade}\nValor: {valor}"
    }
)

st.pydeck_chart(deck)


import busca_empresa

st.subheader("🔎 Busca investigativa por empresa")

empresa = st.text_input("Digite o nome da empresa")

if empresa:

    df_emp, resumo = busca_empresa.buscar_empresa(empresa)

    if df_emp is not None:

        st.write("Resumo da empresa")

        st.write(resumo)

        st.write("Contratos encontrados")

        st.dataframe(df_emp)

    else:

        st.warning("Empresa não encontrada")


import ranking_contas

st.subheader("🚨 Top 10 contas orçamentárias mais suspeitas")

if "df" in locals():

    df_rank = ranking_contas.ranking_contas_suspeitas(df)

    if not df_rank.empty:

        st.dataframe(df_rank)

        st.bar_chart(
            df_rank.set_index("_conta_ref")["score_risco"]
        )


import crescimento_contas

st.subheader("📈 Crescimento anormal por conta (ano a ano)")

if "df" in locals():

    df_cres = crescimento_contas.crescimento_por_conta(df)

    if not df_cres.empty:

        st.dataframe(df_cres[[
            "_conta_ref",
            "ano",
            "_valor_base",
            "crescimento",
            "risco"
        ]])

        st.bar_chart(
            df_cres.set_index("_conta_ref")["crescimento"]
        )


import exportar_relatorio

st.subheader("📄 Exportar relatório da investigação")

if "df" in locals():

    if st.button("Gerar relatório"):

        arquivo = exportar_relatorio.gerar_relatorio(df)

        if arquivo:

            st.success("Relatório gerado")

            with open(arquivo,"rb") as f:
                st.download_button(
                    label="Baixar CSV",
                    data=f,
                    file_name=arquivo
                )


import linha_tempo_gastos

st.subheader("📈 Linha do tempo dos gastos públicos")

if "df" in locals():

    df_tempo = linha_tempo_gastos.linha_tempo_gastos(df)

    if not df_tempo.empty:

        st.dataframe(df_tempo)

        st.line_chart(
            df_tempo.set_index(df_tempo.columns[1])["_valor_base"]
        )


import detectar_picos

st.subheader("🚨 Detector de picos anormais")

if "df_tempo" in locals():

    df_alertas = detectar_picos.detectar_picos(df_tempo)

    st.dataframe(df_alertas)

    picos = df_alertas[df_alertas["alerta"] != "normal"]

    if not picos.empty:
        st.warning("Picos anormais detectados")


import heatmap_gastos

st.subheader("🔥 Heatmap de gastos públicos")

if "df" in locals():

    df_heat = heatmap_gastos.heatmap_gastos(df)

    if not df_heat.empty:

        st.dataframe(df_heat)

        st.write("Mapa de intensidade dos gastos")

        st.bar_chart(df_heat)


import distribuicao_area

st.subheader("📊 Distribuição do orçamento por área")

if "df" in locals():

    df_area = distribuicao_area.distribuicao_por_area(df)

    if not df_area.empty:

        st.dataframe(df_area)

        st.bar_chart(
            df_area.set_index("area")["_valor_base"]
        )
