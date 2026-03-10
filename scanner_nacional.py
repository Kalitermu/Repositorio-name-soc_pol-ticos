import requests
import pandas as pd

def cidades():

    return {
        "São Paulo":"3550308",
        "Guarulhos":"3518800",
        "Itaquaquecetuba":"3523107",
        "Suzano":"3552502",
        "Poá":"3539806",
        "Ferraz de Vasconcelos":"3515707",
        "Santos":"3548500",
        "Praia Grande":"3541000",
        "São Vicente":"3551009"
    }

def coletar():

    resultado = []

    for nome,codigo in cidades().items():

        try:

            url = f"https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?codigo_ibge={codigo}"

            r = requests.get(url,timeout=30)

            dados = r.json()["items"]

            if len(dados) == 0:
                continue

            df = pd.DataFrame(dados)

            if "valor" in df.columns:
                valores = pd.to_numeric(df["valor"],errors="coerce").dropna()
            elif "valor_item" in df.columns:
                valores = pd.to_numeric(df["valor_item"],errors="coerce").dropna()
            else:
                continue

            total = valores.sum()

            media = valores.mean()

            risco = total / media

            resultado.append({

                "cidade":nome,
                "gasto_total":total,
                "media":media,
                "risco":round(risco,2)

            })

        except:
            pass

    return pd.DataFrame(resultado)
