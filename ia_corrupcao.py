import pandas as pd

def analisar_corrupcao(codigo_ibge):

    df = pd.DataFrame({
        "cidade": ["São Paulo"],
        "score": [7.5]
    })

    df["alerta"] = "normal"

    df.loc[df["score"] > 7, "alerta"] = "alto"
    df.loc[df["score"] > 5, "alerta"] = "medio"

    return df
