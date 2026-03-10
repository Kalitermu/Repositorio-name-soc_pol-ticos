import streamlit as st
import pandas as pd
from tesouro_api import buscar_dados_municipio
import detector_cartel

st.title("🔎 Investigação")

cidades = {
    "São Paulo":"3550308",
    "Santos":"3548500",
    "Praia Grande":"3541000",
    "São Vicente":"3551009",
    "Guarujá":"3518701"
}

cidade_nome = st.selectbox("Escolha a cidade", list(cidades.keys()))
codigo = cidades[cidade_nome]

df = buscar_dados_municipio(codigo)

if df.empty:

    st.warning("Não foi possível carregar dados.")

else:

    # detectar coluna de valor automaticamente
    if "valor" in df.columns:
        df["valor_calc"] = pd.to_numeric(df["valor"], errors="coerce")

    elif "valor_item" in df.columns:
        df["valor_calc"] = pd.to_numeric(df["valor_item"], errors="coerce")

    else:
        st.error("Coluna de valor não encontrada.")
        st.write(df.columns)
        st.stop()

    df = df.dropna(subset=["valor_calc"])

    media = df["valor_calc"].mean()

    st.subheader("🚨 Possíveis picos de gasto")

    picos = df[df["valor_calc"] > media * 2]

    if picos.empty:
        st.info("Nenhum pico detectado.")
    else:
        st.dataframe(picos.head(20))

    st.subheader("🔁 Valores repetidos")

    repetidos = df[df["valor_calc"].duplicated(keep=False)]

    if repetidos.empty:
        st.info("Nenhum valor repetido.")
    else:
        st.dataframe(repetidos.head(20))

st.subheader("🔗 Possível cartel de empresas")

df_cartel = detector_cartel.detectar_cartel()

if df_cartel.empty:
    st.info("Nenhuma empresa suspeita encontrada.")
else:
    st.dataframe(df_cartel)
