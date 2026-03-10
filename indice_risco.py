
import pandas as pd

def calcular_indice_risco(df):

    if "_valor_base" not in df.columns:
        return 0

    media = df["_valor_base"].mean()
    desvio = df["_valor_base"].std()

    if desvio == 0:
        return 0

    df["zscore"] = (df["_valor_base"] - media) / desvio

    anomalias = (df["zscore"] > 2).sum()

    proporcao = anomalias / len(df)

    score = min(proporcao * 10, 10)

    return round(score,2)
