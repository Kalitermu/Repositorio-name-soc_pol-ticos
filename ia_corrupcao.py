import pandas as pd

def analisar_corrupcao(df):

    if df.empty:
        return pd.DataFrame()

    valores = pd.to_numeric(df["valor_calc"], errors="coerce").dropna()

    media = valores.mean()
    desvio = valores.std()

    df["alerta"] = "normal"

    df.loc[df["valor_calc"] > media * 2, "alerta"] = "🚨 gasto muito alto"

    repetidos = valores.duplicated(keep=False)

    df.loc[repetidos, "alerta"] = "⚠ valor repetido"

    df["score_risco"] = (df["valor_calc"] / media).round(2)

    return df.sort_values("score_risco", ascending=False)
