import pandas as pd

def analisar(df):

    if df.empty:
        return pd.DataFrame()

    if "valor_calc" in df.columns:
        valores = df["valor_calc"]
    elif "valor" in df.columns:
        valores = df["valor"]
    else:
        return pd.DataFrame()

    media = valores.mean()

    df["indice_risco"] = valores / media

    suspeitos = df[df["indice_risco"] > 2]

    resultado = suspeitos[["indice_risco"]].copy()
    resultado["classificacao"] = "🚨 possivel corrupcao"

    return resultado
