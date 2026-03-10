import requests
import pandas as pd

def buscar_contratos():

    url="https://pncp.gov.br/api/consulta/v1/contratos?pagina=1"

    try:

        r=requests.get(url,timeout=30)

        if r.status_code!=200:
            return pd.DataFrame()

        dados=r.json()

        if "data" not in dados:
            return pd.DataFrame()

        contratos=[]

        for item in dados["data"][:50]:

            contratos.append({
                "orgao":item.get("orgaoEntidade",""),
                "empresa":item.get("razaoSocialFornecedor",""),
                "valor":item.get("valorInicial",""),
                "modalidade":item.get("modalidadeNome","")
            })

        return pd.DataFrame(contratos)

    except:
        return pd.DataFrame()
