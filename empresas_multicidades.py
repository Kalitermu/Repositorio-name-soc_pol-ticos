
import pandas as pd

def empresas_multicidades():

    data = {
        "empresa":[
            "Construtora Alpha",
            "Construtora Alpha",
            "Tech Infra",
            "Tech Infra",
            "Serviços Delta",
            "Serviços Delta"
        ],
        "cidade":[
            "Praia Grande",
            "Santos",
            "São Vicente",
            "Santos",
            "Guarujá",
            "Cubatão"
        ],
        "lat":[
            -24.0058,
            -23.9608,
            -23.9631,
            -23.9608,
            -23.9938,
            -23.8911
        ],
        "lon":[
            -46.4028,
            -46.3336,
            -46.3919,
            -46.3336,
            -46.2564,
            -46.4253
        ]
    }

    df = pd.DataFrame(data)

    contagem = df.groupby("empresa")["cidade"].nunique()

    df_empresas = contagem.reset_index()

    df_empresas.columns = ["empresa","cidades"]

    return df, df_empresas
