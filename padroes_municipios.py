
import pandas as pd

def padroes_municipios():

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
        261000000000,
        50000000000,
        40000000000
        ],
        "contratos":[
        5,
        3,
        5,
        2,
        2
        ]
    }

    df = pd.DataFrame(data)

    media = df["gasto_publico"].mean()

    df["padrao"] = "normal"

    df.loc[df["gasto_publico"] > media * 1.5, "padrao"] = "⚠ gasto muito acima"

    df.loc[df["contratos"] >= 5, "padrao"] = "🚨 padrão de contratos elevado"

    return df
