import requests
import pandas as pd

def buscar_obras():

    contratos = []

    for pagina in range(1,50):

        url = f"https://pncp.gov.br/api/consulta/v1/contratos?pagina={pagina}"

        try:

            r = requests.get(url, timeout=30)
            dados = r.json()

            if not isinstance(dados, list) or len(dados) == 0:
                break

            for item in dados:

                contratos.append({
                    "cidade": item.get("orgaoEntidade", {}).get("municipioNome"),
                    "empresa": item.get("fornecedor", ""),
                    "valor_inicial": item.get("valorInicial", 0),
                    "valor_total": item.get("valorGlobal", 0),
                    "data_inicio": item.get("dataVigenciaInicial", ""),
                    "data_fim": item.get("dataVigenciaFinal", ""),
                    "descricao": item.get("objeto", "")
                })

        except:
            pass

    df = pd.DataFrame(contratos)

    return df
