
import pandas as pd

def contratos_suspeitos():

    data = {
        "cidade":[
            "Praia Grande",
            "Santos",
            "São Vicente"
        ],
        "lat":[
            -24.0058,
            -23.9608,
            -23.9631
        ],
        "lon":[
            -46.4028,
            -46.3336,
            -46.3919
        ],
        "valor":[
            500000000,
            120000000,
            40000000
        ]
    }

    df = pd.DataFrame(data)

    def classificar(valor):

        if valor > 300000000:
            return [255,0,0,160]
        elif valor > 100000000:
            return [255,200,0,160]
        else:
            return [0,200,0,160]

    df["color"] = df["valor"].apply(classificar)

    df["raio"] = df["valor"] / 50000

    return df
