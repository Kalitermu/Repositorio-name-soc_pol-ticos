
import requests
import pandas as pd

def dados_tesouro():

    url = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/resultado"

    r = requests.get(url)

    dados = r.json()

    if "items" in dados:
        df = pd.DataFrame(dados["items"])
        return df

    return pd.DataFrame()
