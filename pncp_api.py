import requests
import pandas as pd

def buscar_contratos():

    url = "https://pncp.gov.br/api/consulta/v1/contratos"

    try:
        r = requests.get(url, timeout=30)

        if r.status_code != 200:
            return pd.DataFrame()

        dados = r.json()

        registros = []

        for item in dados.get("data", [])[:50]:

            registros.append({
                "empresa": item.get("nomeFornecedor"),
                "valor": item.get("valorTotal"),
                "orgao": item.get("orgaoEntidade"),
                "objeto": item.get("objetoContrato")
            })

        df = pd.DataFrame(registros)

        return df

    except Exception:
        return pd.DataFrame()
