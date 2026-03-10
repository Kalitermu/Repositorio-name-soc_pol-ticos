import requests
import pandas as pd

def buscar_dados_municipio(codigo_ibge="3550308"):

    url = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo"

    params = {
        "codigo_ibge": codigo_ibge,
        "limit": 2000
    }

    try:

        r = requests.get(url, params=params, timeout=30)

        if r.status_code != 200:
            return pd.DataFrame()

        dados = r.json().get("items", [])

        if not dados:
            return pd.DataFrame()

        df = pd.DataFrame(dados)

        return df

    except Exception:
        return pd.DataFrame()
