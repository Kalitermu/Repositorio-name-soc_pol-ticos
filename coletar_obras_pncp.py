import requests
import pandas as pd

def buscar_obras():

    contratos = []

    for pagina in range(1, 10):

        url = f"https://pncp.gov.br/api/consulta/v1/contratos?pagina={pagina}"

        try:
            r = requests.get(url, timeout=30)

            if r.status_code != 200:
                continue

            dados = r.json()

            if not isinstance(dados, list):
                continue

            for item in dados:

                contratos.append({
                    "cidade": item.get("orgaoEntidade", {}).get("municipioNome", "desconhecido"),
                    "descricao": item.get("objeto", "contrato público"),
                    "empresa": item.get("fornecedor", "não informado"),
                    "valor_total": item.get("valorGlobal", 0)
                })

        except Exception:
            continue

    df = pd.DataFrame(contratos)

    return df
