
import pandas as pd

def mapa_transparencia():

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
        "score":[
            58,
            72,
            63
        ]
    }

    df = pd.DataFrame(data)

    def cor(score):

        if score >= 70:
            return [0,200,0,160]
        elif score >= 60:
            return [255,200,0,160]
        else:
            return [200,0,0,160]

    df["color"] = df["score"].apply(cor)

    df["raio"] = df["score"] * 2000

    return df
