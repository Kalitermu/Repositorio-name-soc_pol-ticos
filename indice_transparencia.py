
import pandas as pd

def indice_transparencia():

    data = {
        "cidade":[
            "Praia Grande",
            "Santos",
            "São Vicente"
        ],
        "eficiencia_social":[
            0.35,
            0.58,
            0.44
        ],
        "crescimento_gastos":[
            0.18,
            0.12,
            0.31
        ],
        "risco_fiscal":[
            0.2,
            0.1,
            0.3
        ]
    }

    df = pd.DataFrame(data)

    df["score_transparencia"] = (
        (df["eficiencia_social"] * 50) +
        ((1 - df["crescimento_gastos"]) * 30) +
        ((1 - df["risco_fiscal"]) * 20)
    )

    df["score_transparencia"] = df["score_transparencia"].round(2)

    df = df.sort_values(
        "score_transparencia",
        ascending=False
    )

    return df
