
import pandas as pd

def risco_fiscal():

    data = {
        "cidade":[
            "Praia Grande",
            "Santos",
            "São Vicente"
        ],
        "gasto_2023":[
            261559209186,
            120000000000,
            192069221173
        ],
        "previsao_2024":[
            310000000000,
            135000000000,
            220000000000
        ]
    }

    df = pd.DataFrame(data)

    df["crescimento"] = (
        df["previsao_2024"] - df["gasto_2023"]
    ) / df["gasto_2023"]

    def classificar(x):

        if x > 0.35:
            return "🚨 risco alto"
        elif x > 0.20:
            return "⚠ risco moderado"
        else:
            return "normal"

    df["risco_fiscal"] = df["crescimento"].apply(classificar)

    return df
