
import pandas as pd

def heatmap_gastos(df):

    if "_valor_base" not in df.columns:
        return pd.DataFrame()

    if "ano" not in df.columns or "bimestre" not in df.columns:
        return pd.DataFrame()

    tabela = df.pivot_table(
        values="_valor_base",
        index="ano",
        columns="bimestre",
        aggfunc="sum"
    )

    return tabela
