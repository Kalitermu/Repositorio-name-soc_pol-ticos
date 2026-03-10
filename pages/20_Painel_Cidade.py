import streamlit as st
import painel_cidade

st.title("🏙️ Painel Investigativo da Cidade")

codigo = st.text_input(
"Código IBGE",
"3550308"
)

if st.button("Analisar cidade"):

    dados = painel_cidade.gerar_painel(codigo)

    if dados is None:

        st.warning("Não foi possível carregar dados.")

    else:

        st.subheader("📊 Estatísticas")

        st.metric("Orçamento total", f"R$ {dados['total']:,.0f}")
        st.metric("Média de gastos", f"R$ {dados['media']:,.0f}")
        st.metric("Desvio padrão", f"R$ {dados['desvio']:,.0f}")

        st.subheader("🔁 Repetições de valores")

        st.write(dados["repeticoes"])

        st.subheader("🚨 Score de risco")

        st.metric("Score", dados["score"])

        st.subheader("🏢 Empresas com contratos")

        st.dataframe(dados["contratos"])

        st.bar_chart(
            dados["contratos"].set_index("empresa")["valor_total"]
        )
