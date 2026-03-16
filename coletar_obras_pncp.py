import requests
import pandas as pd


def buscar_obras():

    obras = []

    for pagina in range(1, 40):

        url = f"https://pncp.gov.br/api/consulta/v1/contratos?pagina={pagina}"

        try:
            r = requests.get(url, timeout=30)

            if r.status_code != 200:
                continue

            dados = r.json()

            if not isinstance(dados, list):
                continue

            for item in dados:

                cidade = item.get("orgaoEntidade", {}).get("municipioNome", "desconhecido")

                orgao = item.get("orgaoEntidade", {}).get("razaoSocial", "não informado")

                obra = item.get("objeto", "contrato público")

                empresa = item.get("fornecedor", "não informado")

                valor = item.get("valorGlobal", 0)

                obras.append({
                    "cidade": cidade,
                    "orgao": orgao,
                    "obra": obra,
                    "empresa": empresa,
                    "valor": valor
                })

        except Exception:
            continue

    df = pd.DataFrame(obras)

    return df
