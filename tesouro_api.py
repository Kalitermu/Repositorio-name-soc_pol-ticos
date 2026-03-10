import requests
import pandas as pd

def buscar_dados_municipio(codigo_ibge):

    url = f"https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?codigo_ibge={codigo_ibge}"

    try:

        r = requests.get(url, timeout=30)

        if r.status_code != 200:
            return pd.DataFrame()

        dados = r.json()

        if "items" not in dados:
            return pd.DataFrame()

        df = pd.DataFrame(dados["items"])

        return df

    except Exception:
        return pd.DataFrame()
