import streamlit as st
from modules.radar_nacional import gerar_base_nacional

st.title("🏙️ Detalhe da Cidade")

df = gerar_base_nacional()

cidade = st.selectbox(
    "Escolha a cidade",
    df["cidade"]
)

dados = df[df["cidade"] == cidade].iloc[0]

st.subheader("📊 Informações principais")

st.metric("Score de risco", dados["score_risco"])
st.metric("Gasto total", f"R$ {dados['gasto_total']:,}")
st.metric("Repetições de valores", dados["repeticoes"])
st.metric("Concentração de contas", dados["concentracao"])

st.subheader("📈 Comparação com outras cidades")

st.bar_chart(df.set_index("cidade")["score_risco"])

st.subheader("📊 Distribuição de indicadores")

grafico = {
    "repeticoes": dados["repeticoes"],
    "concentracao": dados["concentracao"],
    "desvio": dados["desvio"]
}

st.bar_chart(grafico)


import modules.gerar_relatorio as rel

st.subheader("📄 Relatório Fiscal")

if st.button("Gerar relatório PDF"):

    cidade = dados["cidade"]
    score = dados["score_risco"]
    gasto = dados["gasto_total"]

    arquivo = rel.gerar_pdf(
        cidade,
        score,
        gasto
    )

    with open(arquivo,"rb") as f:
        st.download_button(
            "Baixar PDF",
            f,
            file_name="relatorio_fiscal.pdf"
        )
