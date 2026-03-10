
import pandas as pd

def ranking_eficiencia():

    data = {
        "municipio":[
            "Praia Grande",
            "Santos",
            "São Vicente",
            "Guarujá",
            "Cubatão"
        ],
        "gasto_total":[
            261559209186,
            120000000000,
            192069221173,
            50000000000,
            40000000000
        ],
        "saude":[
            45000000000,
            30000000000,
            40000000000,
            12000000000,
            9000000000
        ],
        "educacao":[
            38000000000,
            28000000000,
            35000000000,
            10000000000,
            8000000000
        ],
        "social":[
            9000000000,
            12000000000,
            11000000000,
            8000000000,
            7000000000
        ]
    }

    df = pd.DataFrame(data)

    df["investimento_social_total"] = (
        df["saude"] +
        df["educacao"] +
        df["social"]
    )

    df["indice_eficiencia"] = (
        df["investimento_social_total"] /
        df["gasto_total"]
    )

    df = df.sort_values(
        "indice_eficiencia",
        ascending=False
    )

    return df
