
import pandas as pd

def analisar_contratos(df):

    if "empresa" not in df.columns or "valor" not in df.columns:
        return pd.DataFrame()

    resumo = (
        df.groupby("empresa")["valor"]
        .agg(["count","sum"])
        .reset_index()
        .rename(columns={"count":"contratos","sum":"valor_total"})
        .sort_values("valor_total",ascending=False)
    )

    return resumo
