import requests
import pandas as pd

def buscar_contratos():

    url = "https://pncp.gov.br/api/consulta/v1/contratos?pagina=1&tamanhoPagina=50"

    try:

        r = requests.get(url, timeout=30)

        if r.status_code != 200:
            return pd.DataFrame()

        dados = r.json()

        contratos = []

        lista = dados.get("data", [])

        for item in lista:

            empresa = item.get("nomeFornecedor", "Não informado")
            objeto = item.get("objetoCompra", "Não informado")
            valor = item.get("valorTotalEstimado", 0)

            contratos.append({
                "empresa": empresa,
                "objeto": objeto,
                "valor": valor
            })

        df = pd.DataFrame(contratos)

        return df

    except Exception:
        return pd.DataFrame()
