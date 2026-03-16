import requests
import pandas as pd


def buscar_obras():

    URL = "https://pncp.gov.br/api/consulta/v1/contratos"

    try:

        r = requests.get(URL, timeout=30)
        dados = r.json()

        contratos = []

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

        df = pd.DataFrame(contratos)

        return df

    except:
        return pd.DataFrame()
