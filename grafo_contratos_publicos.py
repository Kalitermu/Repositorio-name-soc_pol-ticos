import pandas as pd

def gerar_grafo(df):

    conexoes = []

    for _, row in df.iterrows():

        origem = row["orgao"] if "orgao" in df.columns else row.get("cidade","desconhecido")
        destino = row["empresa"] if "empresa" in df.columns else "Empresa Pública"

        conexoes.append({
            "origem": origem,
            "destino": destino,
            "valor": row.get("valor",1)
        })

    return pd.DataFrame(conexoes)
