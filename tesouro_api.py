import requests
import pandas as pd

def buscar_dados_municipio(codigo_ibge="3550308"):
    url = f"https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?codigo_ibge={codigo_ibge}"

    try:
        r = requests.get(url, timeout=30)
        dados = r.json()["items"]

        df = pd.DataFrame(dados)

        return df

    except Exception as e:
        return pd.DataFrame()
