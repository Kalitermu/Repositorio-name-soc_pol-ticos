
import requests
import pandas as pd

def contratos_pncp():

    url = "https://pncp.gov.br/api/consulta/v1/contratos"

    params = {
        "pagina":1,
        "tamanhoPagina":10
    }

    r = requests.get(url,params=params)

    dados = r.json()

    if "data" in dados:
        df = pd.DataFrame(dados["data"])
        return df

    return pd.DataFrame()
