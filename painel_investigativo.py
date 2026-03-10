
import pandas as pd

def painel_investigativo():

    data = {
        "municipio":[
        "São Vicente",
        "Santos",
        "Praia Grande",
        "Guarujá",
        "Cubatão"
        ],
        "gasto_publico":[
        192000000000,
        120000000000,
        80000000000,
        50000000000,
        40000000000
        ],
        "contratos_empresa":[
        5,
        3,
        2,
        4,
        3
        ]
    }

    df = pd.DataFrame(data)

    media = df["gasto_publico"].mean()

    df["alerta"] = "normal"

    df.loc[df["gasto_publico"] > media * 1.5, "alerta"] = "⚠ gasto acima da média"

    df.loc[df["contratos_empresa"] >= 4, "alerta"] = "🚨 concentração de contratos"

    return df
