import requests
import pandas as pd


def buscar_contratos():

    url = "https://pncp.gov.br/api/consulta/v1/contratos"

    try:
        r = requests.get(url, timeout=30)

        if r.status_code != 200:
            return pd.DataFrame()

        dados = r.json()

        contratos = []

        # PNCP normalmente retorna {"data": [...]}
        lista = dados.get("data", [])

        for item in lista[:50]:

            cidade = item.get("orgaoEntidade", {}).get("municipioNome", "N/A")
            obra = item.get("objeto", "N/A")
            empresa = item.get("fornecedor", "N/A")
            valor = item.get("valorGlobal", 0)

            contratos.append({
                "cidade": cidade,
                "obra": obra,
                "empresa": empresa,
                "valor": valor
            })

        df = pd.DataFrame(contratos)

        return df

    except Exception:
        return pd.DataFrame()
