import streamlit as st
import contratos

st.title("🏢 Contratos Públicos")

st.write("""
Análise de contratos e empresas.

Esta página mostra:
- empresas que mais recebem contratos
- concentração de fornecedores
- ranking de contratos
- comparação de valores
""")

df = contratos.empresas_suspeitas()

if df.empty:

    st.warning("Nenhum contrato encontrado.")

else:

    st.subheader("📊 Ranking de empresas")

    st.dataframe(df)

    st.subheader("📈 Distribuição de contratos")

    st.bar_chart(df.set_index("empresa")["valor_total"])
