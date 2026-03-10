import pandas as pd

def analisar(df):

    if df.empty:
        return pd.DataFrame()

    # detectar coluna de valor
    if "valor_calc" in df.columns:
        valores = df["valor_calc"]
    elif "valor" in df.columns:
        valores = df["valor"]
    else:
        return pd.DataFrame()

    media = valores.mean()
    desvio = valores.std()

    df["indice_anomalia"] = valores / media

    suspeitos = df[
        (df["indice_anomalia"] > 3) |
        (valores > media + 2*desvio)
    ]

    resultado = suspeitos.copy()

    resultado["alerta"] = "🚨 gasto muito acima da média"

    return resultado
