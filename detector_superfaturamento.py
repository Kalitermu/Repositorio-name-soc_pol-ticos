
import pandas as pd

def detectar_superfaturamento(df):

    if "valor" not in df.columns:
        return pd.DataFrame()

    df = df.copy()

    media = df["valor"].mean()
    desvio = df["valor"].std()

    if desvio == 0:
        df["zscore"] = 0
    else:
        df["zscore"] = (df["valor"] - media) / desvio

    def classificar(z):
        if z >= 3:
            return "🚨 possível superfaturamento"
        elif z >= 2:
            return "⚠ valor alto"
        else:
            return "normal"

    df["alerta"] = df["zscore"].apply(classificar)

    return df.sort_values("zscore", ascending=False)
