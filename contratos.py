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
