import pandas as pd

def analisar():

    df = pd.DataFrame({

        "cidade":[
        "São Paulo",
        "Guarulhos",
        "Santos",
        "Praia Grande",
        "Suzano"
        ],

        "obra":[
        "pavimentacao",
        "pavimentacao",
        "pavimentacao",
        "pavimentacao",
        "pavimentacao"
        ],

        "valor":[
        5000000,
        5200000,
        5100000,
        14000000,
        5300000
        ]

    })

    media = df.groupby("obra")["valor"].mean().reset_index()
    media = media.rename(columns={"valor":"media_obra"})

    df = df.merge(media,on="obra")

    df["indice"] = df["valor"] / df["media_obra"]

    suspeitos = df[df["indice"] > 2]

    return suspeitos
