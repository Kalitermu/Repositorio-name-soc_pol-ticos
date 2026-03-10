import streamlit as st

st.markdown("""

<style>

.stApp {background-color: #ffb347;}

</style>

""", unsafe_allow_html=True)

import streamlit as st

st.markdown("""<style>

h1 {color:#FFA500;}

</style>""", unsafe_allow_html=True)



import streamlit as st
st.set_page_config(layout='wide')

import painel_nacional

st.subheader("🌎 Radar Nacional de Transparência")

df_nat = painel_nacional.dados_nacionais()

st.dataframe(df_nat)

st.bar_chart(df_nat.set_index("municipio")["risco"])

import streamlit as st

st.set_page_config(layout="wide")

st.title("🚨 Radar Transparência Pública")

menu = st.sidebar.selectbox(
"Análise",
[
"Radar Fiscal",
"Contratos Públicos",
"Detector de Corrupção",
"Mapa Nacional",
"Ranking Nacional",
"Programas Sociais",
"Painel Investigativo",
"Redes de Contratos",
"Distribuição do Dinheiro"
]
)

if menu == "Radar Fiscal":
    import risco_fiscal

elif menu == "Contratos Públicos":
    import contratos

elif menu == "Detector de Corrupção":
    import detector_corrupcao

elif menu == "Mapa Nacional":
    import mapa_brasil

elif menu == "Ranking Nacional":
    import ranking_nacional

elif menu == "Programas Sociais":
    import programas_sociais

elif menu == "Painel Investigativo":
    import painel_investigativo

elif menu == "Redes de Contratos":
    import redes_suspeitas

elif menu == "Distribuição do Dinheiro":
    import distribuicao_dinheiro



import detector_superfaturamento

st.subheader("🚨 Detector de possível superfaturamento")

df_super = detector_superfaturamento.detectar_superfaturamento()

st.dataframe(df_super)



import detector_rede_empresas

st.subheader("🧠 Empresas com contratos em vários municípios")

df_rede = detector_rede_empresas.detectar_rede()

st.dataframe(df_rede)

st.bar_chart(df_rede.set_index("empresa")["valor_total"])



import traduzir_contas

st.subheader("📊 Destino do dinheiro público")

try:
    df["area"] = df["_conta_ref"].apply(traduzir_contas.traduzir_conta)

    destino = df.groupby("area")["_valor_base"].sum().reset_index()

    st.dataframe(destino)
    st.bar_chart(destino.set_index("area")["_valor_base"])

except:
    st.info("Ainda não foi possível identificar o destino das contas.")

