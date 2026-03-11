import pandas as pd

def carregar_base():

    dados = [
        {
            "orgao":"Prefeitura de Praia Grande",
            "empresa":"Engenharia Brasil",
            "valor":1200000
        },
        {
            "orgao":"Prefeitura de Santos",
            "empresa":"Construtora Alpha",
            "valor":3500000
        },
        {
            "orgao":"Prefeitura de São Vicente",
            "empresa":"Obras Litoral",
            "valor":800000
        }
    ]

    df = pd.DataFrame(dados)

    if "orgao" not in df.columns:
        df["orgao"] = "Não informado"

    if "empresa" not in df.columns:
        df["empresa"] = "Empresa desconhecida"

    if "valor" not in df.columns:
        df["valor"] = 0

    return df
