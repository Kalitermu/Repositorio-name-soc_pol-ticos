
import pandas as pd

def investimentos_areas():

    data = {
        "municipio":[
            "Praia Grande",
            "Santos",
            "São Vicente"
        ],
        "saude":[45000000000,30000000000,40000000000],
        "educacao":[38000000000,28000000000,35000000000],
        "obras":[52000000000,20000000000,33000000000],
        "seguranca":[12000000000,8000000000,9000000000],
        "social":[9000000000,12000000000,11000000000]
    }

    df = pd.DataFrame(data)

    df["total"] = (
        df["saude"] +
        df["educacao"] +
        df["obras"] +
        df["seguranca"] +
        df["social"]
    )

    return df
