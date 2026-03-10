
import pandas as pd

def detectar_irregularidades(df):

    media = df["valor"].mean()

    alertas = []

    for empresa, grupo in df.groupby("empresa"):

        total = grupo["valor"].sum()

        if total > media * 3:
            alertas.append({
                "empresa": empresa,
                "motivo": "valor muito acima da média",
                "total": total
            })

        if len(grupo) >= 3:
            alertas.append({
                "empresa": empresa,
                "motivo": "empresa repetida em vários contratos",
                "total": total
            })

    return pd.DataFrame(alertas)
