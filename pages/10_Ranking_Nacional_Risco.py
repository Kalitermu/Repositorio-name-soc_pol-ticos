import streamlit as st
import pandas as pd

st.title("🇧🇷 Ranking Nacional de Risco Fiscal")

dados = pd.DataFrame({
    "cidade":[
        "São Vicente",
        "Praia Grande",
        "Santos",
        "Campinas",
        "São Paulo"
    ],
    "estado":[
        "SP",
        "SP",
        "SP",
        "SP",
        "SP"
    ],
    "score":[
        6.7,
        5.9,
        4.1,
        3.8,
        3.2
    ]
})

dados = dados.sort_values("score", ascending=False)

st.dataframe(dados)

st.bar_chart(dados.set_index("cidade")["score"])
