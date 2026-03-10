import pandas as pd

def rastrear(df):

    if df.empty:
        return pd.DataFrame()

    if "conta" not in df.columns:
        return pd.DataFrame()

    resumo = df.groupby("conta")["valor_calc"].sum().reset_index()

    resumo = resumo.sort_values("valor_calc", ascending=False)

    return resumo
