import pandas as pd
import requests

def buscar_contratos():

    url = "https://pncp.gov.br/api/consulta/v1/contratos"

    try:
        r = requests.get(url, timeout=30)
        dados = r.json()

        if "data" not in dados or len(dados["data"]) == 0:
            raise Exception("sem dados")

        df = pd.DataFrame(dados["data"])

        return df

    except:

        # fallback com dados exemplo
        df = pd.DataFrame({
            "cidade": [
                "São Paulo",
                "Santos",
                "Praia Grande",
                "Guarujá"
            ],
            "empresa": [
                "Construtora Alpha",
                "Engenharia Brasil",
                "Obras Litoral",
                "Construtora Beta"
            ],
            "valor": [
                8500000,
                4200000,
                2100000,
                1900000
            ]
        })

        return df
