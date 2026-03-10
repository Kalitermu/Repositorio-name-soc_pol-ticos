import streamlit as st
import pandas as pd

st.title("👨‍👩‍👧 Benefícios Sociais")

st.write("Análise de distribuição de benefícios.")

dados = pd.DataFrame({
    "cidade":[
        "São Vicente",
        "Praia Grande",
        "Santos",
        "Guarujá",
        "Cubatão"
    ],
    "familias":[
        32000,
        21000,
        18000,
        25000,
        15000
    ],
    "valor_total":[
        28000000,
        18000000,
        16000000,
        21000000,
        12000000
    ]
})

dados["valor_medio"] = dados["valor_total"] / dados["familias"]

st.subheader("📊 Famílias beneficiadas")

st.dataframe(dados)

st.subheader("📈 Distribuição por cidade")

st.bar_chart(dados.set_index("cidade")["familias"])

st.subheader("💰 Valor médio por família")

st.bar_chart(dados.set_index("cidade")["valor_medio"])
