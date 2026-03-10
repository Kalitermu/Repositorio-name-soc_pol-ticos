import pandas as pd
import base_contratos

def detectar_alertas():

    df = base_contratos.carregar_base()

    alertas = []

    # concentração de empresa
    ranking = df.groupby("empresa")["valor"].sum().reset_index()

    media = ranking["valor"].mean()

    for _,row in ranking.iterrows():

        if row["valor"] > media * 3:

            alertas.append({
                "tipo":"Concentração de contratos",
                "empresa":row["empresa"],
                "valor":row["valor"]
            })

    # valores muito altos
    media_valor = df["valor"].mean()

    for _,row in df.iterrows():

        if row["valor"] > media_valor * 5:

            alertas.append({
                "tipo":"Contrato muito acima da média",
                "empresa":row["empresa"],
                "valor":row["valor"]
            })

    return pd.DataFrame(alertas)
