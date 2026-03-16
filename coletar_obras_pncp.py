import requests
import pandas as pd

def buscar_obras():

    contratos = []

    for pagina in range(1,20):

        url = f"https://pncp.gov.br/api/consulta/v1/contratos?pagina={pagina}"

        try:

            r = requests.get(url, timeout=30)
            dados = r.json()

            if not isinstance(dados, list):
                continue

            for item in dados:

                contratos.append({

                    "cidade": item.get("orgaoEntidade", {}).get("municipioNome"),

                    "descricao": item.get("objeto",""),

                    "empresa": item.get("fornecedor",""),

                    "valor_total": item.get("valorGlobal",0)

                })

        except:
            pass

    df = pd.DataFrame(contratos)

    return df
