
import pandas as pd

def detectar_valores_parecidos():

    data = {
        "empresa":[
            "Construtora Alpha",
            "Construtora Alpha",
            "Tech Infra",
            "Tech Infra",
            "Serviços Delta",
            "Serviços Delta"
        ],
        "valor":[
            4990000,
            5010000,
            10000000,
            10050000,
            2000000,
            2100000
        ]
    }

    df = pd.DataFrame(data)

    df["grupo_valor"] = (df["valor"] // 1000000)

    contagem = df.groupby("grupo_valor").size().reset_index(name="contratos")

    contagem["risco"] = contagem["contratos"].apply(
        lambda x: "🚨 valores muito repetidos" if x >= 3 else ("⚠ possível fracionamento" if x == 2 else "normal")
    )

    return df, contagem
