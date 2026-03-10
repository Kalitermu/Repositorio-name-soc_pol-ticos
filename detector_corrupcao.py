import pandas as pd

def detectar_irregularidades(df):

    if df.empty:
        return pd.DataFrame()

    media = df["valor_total"].mean()

    def risco(valor):

        if valor > media * 2:
            return "🚨 alto risco"

        elif valor > media:
            return "⚠ atenção"

        else:
            return "normal"

    df["alerta"] = df["valor_total"].apply(risco)

    return df
