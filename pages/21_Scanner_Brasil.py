import streamlit as st
import scanner_brasil

st.title("🛰️ Scanner Nacional de Municípios")

st.write("Análise automática de risco fiscal em municípios.")

df=scanner_brasil.executar()

if df.empty:

    st.warning("Nenhum dado encontrado.")

else:

    st.subheader("🏆 Ranking de risco")

    st.dataframe(df)

    st.bar_chart(df.set_index("cidade")["score"])
