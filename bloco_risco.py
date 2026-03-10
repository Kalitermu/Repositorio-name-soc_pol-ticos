
import pandas as pd

def calcular_risco(df):

    media = df["_valor_base"].mean()
    desvio = df["_valor_base"].std()

    df["zscore"] = (df["_valor_base"] - media) / desvio

    df["risco"] = "Normal"
    df.loc[df["zscore"] > 1, "risco"] = "Atenção"
    df.loc[df["zscore"] > 2, "risco"] = "ALTO RISCO"

    return df
