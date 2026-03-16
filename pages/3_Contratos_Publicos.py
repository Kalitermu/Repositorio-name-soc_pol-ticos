import streamlit as st
import contratos
import detector_corrupcao

st.title("🏢 Contratos Públicos")

st.write("""
Análise de contratos e empresas.

Esta página mostra:
- empresas que mais recebem contratos
- concentração de fornecedores
- ranking de contratos
- comparação de valores
""")

# buscar dados reais
df = contratos.buscar_contratos()

if df.empty:

    st.warning("Nenhum contrato encontrado.")

else:

    st.subheader("📊 Ranking de empresas")

    ranking = (
        df.groupby("empresa")["valor"]
        .sum()
        .reset_index()
        .sort_values("valor", ascending=False)
    )

    st.dataframe(ranking)

    st.subheader("🚨 Detector de irregularidades")

    alertas = detector_corrupcao.detectar_irregularidades(df)

    st.dataframe(alertas)

    st.subheader("📈 Distribuição de contratos")

    st.bar_chart(ranking.set_index("empresa")["valor"])
