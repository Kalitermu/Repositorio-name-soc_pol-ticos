import pandas as pd

def analisar(df):

    if df is None or len(df) == 0:
        return pd.DataFrame()

    resultados = []

    for _, row in df.iterrows():

        risco = row.get("risco", row.get("score", 1))

        if risco > 8:
            alerta = "alto"
        elif risco > 5:
            alerta = "medio"
        else:
            alerta = "normal"

        resultados.append({
            "cidade": row.get("cidade","desconhecido"),
            "score": risco,
            "alerta": alerta
        })

    return pd.DataFrame(resultados)
