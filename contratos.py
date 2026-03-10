import pandas as pd

def empresas_suspeitas():

    dados = pd.DataFrame({
        "empresa":[
            "Construtora Alpha",
            "Construtora Beta",
            "Engenharia Brasil",
            "Obras Litoral"
        ],
        "valor":[
            5000000,
            7000000,
            3000000,
            2500000
        ]
    })

    df = dados.sort_values("valor",ascending=False)

    df = df.rename(columns={
        "valor":"valor_total"
    })

    return df
