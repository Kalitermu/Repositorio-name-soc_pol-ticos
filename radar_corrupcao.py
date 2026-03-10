
import pandas as pd

def radar_corrupcao(df):

    resultados = []

    if "valor" not in df.columns:
        return pd.DataFrame()

    media = df["valor"].mean()

    for _,row in df.iterrows():

        risco = "normal"

        if row["valor"] > media * 3:
            risco = "🚨 valor muito acima da média"

        resultados.append({
            "empresa":row.get("razaoSocial","desconhecida"),
            "valor":row["valor"],
            "risco":risco
        })

    df_risco = pd.DataFrame(resultados)

    return df_risco
