import pandas as pd

def analisar(df):

    if df.empty:
        return pd.DataFrame()

    resultados = df.copy()

    media = resultados["valor_calc"].mean()

    resultados["alerta"] = "normal"

    resultados.loc[resultados["valor_calc"] > media * 2, "alerta"] = "🚨 pico de gasto"

    repetidos = resultados["valor_calc"].duplicated(keep=False)

    resultados.loc[repetidos, "alerta"] = "⚠ valor repetido"

    return resultados
