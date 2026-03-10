
import requests
import pandas as pd

def dados_transparencia(api_key):

    url = "https://api.portaldatransparencia.gov.br/api-de-dados/licitacoes"

    headers = {
        "accept":"application/json",
        "chave-api-dados":api_key
    }

    params = {
        "pagina":1
    }

    r = requests.get(url,headers=headers,params=params)

    dados = r.json()

    if isinstance(dados,list):

        df = pd.DataFrame(dados)

        return df

    else:
        return pd.DataFrame({"erro":[dados]})
