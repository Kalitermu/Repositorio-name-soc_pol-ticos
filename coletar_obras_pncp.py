import requests
import pandas as pd

def buscar_obras():

    url = "https://pncp.gov.br/api/consulta/v1/contratos"

    try:

        r = requests.get(url, timeout=30)

        dados = r.json()

        contratos = []

        for item in dados:

            contratos.append({

                "cidade": item.get("orgaoEntidade",{}).get("municipioNome",""),
                "empresa": item.get("fornecedor",""),
                "valor": item.get("valorTotal",0),
                "descricao": item.get("objeto","")

            })

        df = pd.DataFrame(contratos)

        return df

    except:

        return pd.DataFrame()
