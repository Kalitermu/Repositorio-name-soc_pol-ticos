
import pandas as pd

def indice_social():

    data = {
        "cidade":[
        "Praia Grande",
        "Santos",
        "São Vicente"
        ],
        "gasto_publico":[
        261000000000,
        120000000000,
        192000000000
        ],
        "beneficios":[
        9000000,
        12000000,
        11000000
        ]
    }

    df = pd.DataFrame(data)

    df["indice_social"] = df["beneficios"] / df["gasto_publico"]

    return df
