
import pandas as pd

def empresas_suspeitas():

    data = {
        "empresa":[
        "Construtora Alpha",
        "Construtora Beta",
        "Serviços Delta",
        "Construtora Alpha",
        "Construtora Alpha",
        "Serviços Delta",
        "Tech Infra"
        ],
        "valor":[50000000,20000000,15000000,70000000,90000000,20000000,10000000]
    }

    df = pd.DataFrame(data)

    ranking = df.groupby("empresa")["valor"].sum().sort_values(ascending=False)

    return ranking.reset_index()
