import pandas as pd

def detectar_superfaturamento():

    dados = pd.DataFrame({
        "cidade":[
            "Santos",
            "São Vicente",
            "Praia Grande",
            "Guarujá"
        ],
        "obra":[
            "pavimentacao",
            "pavimentacao",
            "pavimentacao",
            "pavimentacao"
        ],
        "valor":[
            3000000,
            8200000,
            3500000,
            3200000
        ]
    })

    media = dados.groupby("obra")["valor"].mean().reset_index()
    media = media.rename(columns={"valor":"media_obra"})

    df = dados.merge(media,on="obra")

    df["indice"] = df["valor"]/df["media_obra"]

    suspeitos = df[df["indice"] > 1.8]

    return suspeitos
