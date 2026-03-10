
import pandas as pd

def detectar_anomalias(df):

    media = df["_valor_base"].mean()
    desvio = df["_valor_base"].std()

    df["zscore"] = (df["_valor_base"] - media) / desvio

    df["alerta"] = "normal"

    df.loc[df["zscore"] > 3, "alerta"] = "🚨 anomalia extrema"
    df.loc[(df["zscore"] > 2) & (df["zscore"] <= 3), "alerta"] = "⚠ valor suspeito"

    return df
