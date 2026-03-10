
import pandas as pd
from indice_risco import calcular_indice_risco

def ranking_cidades(dados):

    resultados = []

    for cidade, df in dados.items():

        score = calcular_indice_risco(df)

        resultados.append({
            "cidade":cidade,
            "score":score
        })

    ranking = pd.DataFrame(resultados)

    ranking = ranking.sort_values("score", ascending=False)

    return ranking
