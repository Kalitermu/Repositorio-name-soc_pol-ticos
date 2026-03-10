
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def prever_gastos():

    data = {
        "ano":[2019,2020,2021,2022,2023],
        "Praia Grande":[80000000000,110000000000,150000000000,190000000000,261559209186],
        "Santos":[70000000000,85000000000,95000000000,110000000000,120000000000],
        "São Vicente":[60000000000,80000000000,120000000000,160000000000,192069221173]
    }

    df = pd.DataFrame(data)

    previsoes = []

    for cidade in df.columns[1:]:

        X = df[["ano"]]
        y = df[cidade]

        modelo = LinearRegression()
        modelo.fit(X,y)

        previsao = modelo.predict([[2024]])[0]

        previsoes.append({
            "cidade":cidade,
            "previsao_2024":int(previsao)
        })

    df_prev = pd.DataFrame(previsoes)

    return df_prev
