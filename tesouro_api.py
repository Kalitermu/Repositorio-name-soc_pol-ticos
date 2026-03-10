import requests
import pandas as pd

def dados_simulados():

    return pd.DataFrame({
        "conta":[
            "Saúde",
            "Educação",
            "Urbanismo",
            "Assistência Social",
            "Administração"
        ],
        "valor":[
            220000000,
            310000000,
            180000000,
            90000000,
            150000000
        ]
    })

def buscar_dados_municipio(codigo_ibge):

    url=f"https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo_anexo13?codigo_ibge={codigo_ibge}"

    try:

        r=requests.get(url,timeout=30)

        if r.status_code!=200:
            return dados_simulados()

        dados=r.json()

        if "items" not in dados:
            return dados_simulados()

        df=pd.DataFrame(dados["items"])

        if df.empty:
            return dados_simulados()

        return df

    except:
        return dados_simulados()
