
import pandas as pd

def linha_tempo_gastos(df):

    # Espera colunas: _valor_base, ano, bimestre (ou mes)
    if "_valor_base" not in df.columns:
        return pd.DataFrame()

    tempo_col = None

    if "bimestre" in df.columns:
        tempo_col = "bimestre"
    elif "mes" in df.columns:
        tempo_col = "mes"

    if tempo_col is None or "ano" not in df.columns:
        return pd.DataFrame()

    grupo = (
        df.groupby(["ano", tempo_col])["_valor_base"]
        .sum()
        .reset_index()
        .sort_values(["ano", tempo_col])
    )

    return grupo
