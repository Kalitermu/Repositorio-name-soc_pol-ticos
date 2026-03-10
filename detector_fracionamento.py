import pandas as pd

def analisar():

    df = pd.DataFrame({

        "orgao":[
        "Prefeitura A",
        "Prefeitura A",
        "Prefeitura A",
        "Prefeitura B",
        "Prefeitura B"
        ],

        "empresa":[
        "Construtora Alpha",
        "Construtora Alpha",
        "Construtora Alpha",
        "Servicos Beta",
        "Servicos Beta"
        ],

        "data":[
        "2024-01-10",
        "2024-01-12",
        "2024-01-14",
        "2024-02-01",
        "2024-02-03"
        ],

        "valor":[
        49000,
        48500,
        49200,
        150000,
        160000
        ]

    })

    df["data"] = pd.to_datetime(df["data"])

    resumo = df.groupby(["orgao","empresa"]).agg(
        qtd_contratos=("valor","count"),
        valor_total=("valor","sum")
    ).reset_index()

    suspeitos = resumo[
        (resumo["qtd_contratos"] >= 3) &
        (resumo["valor_total"] < 200000)
    ]

    suspeitos["alerta"] = "🚨 possível fracionamento"

    return suspeitos
