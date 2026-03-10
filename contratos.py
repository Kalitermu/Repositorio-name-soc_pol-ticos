import pandas as pd

def empresas_suspeitas():

    dados = {
        "empresa":[
            "Construtora Alpha",
            "Construtora Beta",
            "Engenharia Brasil",
            "Infra Litoral",
            "Construtora Alpha",
            "Infra Litoral"
        ],
        "valor":[
            5000000,
            7000000,
            3000000,
            2500000,
            8000000,
            4000000
        ]
    }

    df = pd.DataFrame(dados)

    ranking = df.groupby("empresa")["valor"].sum().reset_index()

    ranking = ranking.rename(columns={"valor":"valor_total"})

    ranking = ranking.sort_values("valor_total",ascending=False)

    return ranking
