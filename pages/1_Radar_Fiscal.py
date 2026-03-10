import streamlit as st
import pandas as pd
from tesouro_api import buscar_dados_municipio
import rastreador_dinheiro

st.title("🚨 Radar Fiscal")

st.write("Consulta de orçamento público direto do Tesouro Nacional.")

codigo = st.text_input(
"Código IBGE do município",
"3550308"
)

if st.button("Consultar"):

    df = buscar_dados_municipio(codigo)

    if df.empty:

        st.warning("Não foi possível carregar dados do Tesouro Nacional.")

    else:

        if "valor" in df.columns:
            valores = pd.to_numeric(df["valor"], errors="coerce")

        elif "valor_item" in df.columns:
            valores = pd.to_numeric(df["valor_item"], errors="coerce")

        else:
            st.error("Coluna de valor não encontrada.")
            st.write(df.columns)
            st.stop()

        valores = valores.dropna()

        total = valores.sum()
        media = valores.mean()
        desvio = valores.std()

        st.subheader("📊 Estatísticas")

        st.metric("Somatório do orçamento", f"R$ {total:,.0f}")
        st.metric("Média de gastos", f"R$ {media:,.0f}")
        st.metric("Desvio padrão", f"R$ {desvio:,.0f}")

        df["valor_calc"] = valores

        top = df.sort_values("valor_calc", ascending=False).head(10)

        st.subheader("📋 Principais contas")

        st.dataframe(top)

        st.subheader("📈 Distribuição de despesas")

        st.bar_chart(top["valor_calc"])

        st.subheader("💰 Para onde vai o dinheiro público")

        destino = rastreador_dinheiro.rastrear(df)

        if destino.empty:
            st.info("Não foi possível identificar as contas.")
        else:
            st.dataframe(destino.head(20))
            st.bar_chart(destino.set_index("conta")["valor_calc"])
