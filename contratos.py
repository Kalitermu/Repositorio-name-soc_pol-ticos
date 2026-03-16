import pandas as pd

def empresas_suspeitas():

    dados = {
        "empresa": [
            "Construtora Alpha",
            "Construtora Beta",
            "Engenharia Brasil",
            "Infra Litoral",
            "Construtora Alpha",
            "Infra Litoral"
        ],

        "valor_total": [
            5000000,
            7000000,
            3000000,
            2500000,
            8000000,
            4000000
        ]
    }

    df = pd.DataFrame(dados)

    ranking = (
        df.groupby("empresa")["valor_total"]
        .sum()
        .reset_index()
    )

    ranking = ranking.sort_values(
        "valor_total",
        ascending=False
    )

    return ranking
st.subheader("🔎 Investigação de contratos")

# empresa que mais ganha
ranking_empresas = (
    df_obras.groupby("empresa")["valor"]
    .agg(["count","sum"])
    .reset_index()
)

ranking_empresas = ranking_empresas.sort_values(
    "sum",
    ascending=False
)

ranking_empresas.columns = [
    "empresa",
    "quantidade_contratos",
    "valor_total"
]

st.write("Empresas que mais recebem dinheiro público")

st.dataframe(ranking_empresas)


# possível favorecimento
suspeitas = ranking_empresas[
    ranking_empresas["quantidade_contratos"] > 3
]

st.subheader("🚨 Possível concentração de contratos")

st.dataframe(suspeitas)


# valor médio de obras
media_obras = df_obras["valor"].mean()

st.subheader("💰 Comparação de valores")

df_obras["alerta"] = df_obras["valor"].apply(
    lambda x: "⚠️ valor acima da média"
    if x > media_obras * 2 else "normal"
)

st.dataframe(df_obras)
