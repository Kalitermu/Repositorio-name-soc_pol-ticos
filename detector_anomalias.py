
import pandas as pd

def detectar_anomalias(df):

    if "_valor_base" not in df.columns:
        return pd.DataFrame()

    df = df.copy()

    media = df["_valor_base"].mean()
    desvio = df["_valor_base"].std()

    if desvio == 0:
        df["zscore"] = 0
    else:
        df["zscore"] = (df["_valor_base"] - media) / desvio

    def classificar(z):
        if z >= 3:
            return "🚨 anomalia alta"
        elif z >= 2:
            return "⚠ atenção"
        else:
            return "normal"

    df["alerta"] = df["zscore"].apply(classificar)

    return df.sort_values("zscore", ascending=False)
