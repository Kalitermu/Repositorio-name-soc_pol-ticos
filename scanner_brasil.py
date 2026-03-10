import pandas as pd
import tesouro_api
import municipios_brasil

def calcular_score(valores):

    media=valores.mean()
    desvio=valores.std()

    score=0

    if desvio>media:
        score+=3

    if valores.duplicated().sum()>5:
        score+=2

    if valores.max()>media*5:
        score+=4

    return score

def executar():

    resultados=[]

    for cidade,codigo in municipios_brasil.municipios.items():

        df=tesouro_api.buscar_dados_municipio(codigo)

        if df.empty:
            continue

        if "valor" in df.columns:
            valores=pd.to_numeric(df["valor"],errors="coerce")

        elif "valor_item" in df.columns:
            valores=pd.to_numeric(df["valor_item"],errors="coerce")

        else:
            continue

        valores=valores.dropna()

        if valores.empty:
            continue

        score=calcular_score(valores)

        resultados.append({
            "cidade":cidade,
            "score":score
        })

    return pd.DataFrame(resultados).sort_values("score",ascending=False)
