
import pandas as pd

def mapa_investimentos():

    data = {
        "municipio":[
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
        "saude":[
            45000000000,
            30000000000,
            40000000000
        ],
        "educacao":[
            38000000000,
            28000000000,
            35000000000
        ],
        "obras":[
            52000000000,
            20000000000,
            33000000000
        ]
    }

    df = pd.DataFrame(data)

    df["total"] = df["saude"] + df["educacao"] + df["obras"]

    df["raio"] = df["total"] / 10000000

    return df
