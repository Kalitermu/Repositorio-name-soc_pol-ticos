import pandas as pd

def gerar_grafo(df):

    if df.empty:
        return pd.DataFrame()

    conexoes = []

    for _,row in df.iterrows():

        conexoes.append({
            "origem":row["orgao"],
            "destino":row["empresa"],
            "valor":row["valor"]
        })

    return pd.DataFrame(conexoes)
