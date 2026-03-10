
import pandas as pd

def top_despesas(df):

    if "_conta_ref" not in df.columns or "_valor_base" not in df.columns:
        return pd.DataFrame()

    ranking = (
        df.groupby("_conta_ref")["_valor_base"]
        .sum()
        .reset_index()
        .sort_values("_valor_base",ascending=False)
        .head(10)
    )

    return ranking
