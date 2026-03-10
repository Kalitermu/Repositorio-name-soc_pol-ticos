
import pandas as pd

def ranking_municipios():

    data = {
        "municipio":[
        "São Vicente",
        "Santos",
        "Praia Grande",
        "Guarujá",
        "Cubatão",
        "São Paulo",
        "Rio de Janeiro",
        "Brasília"
        ],
        "risco":[7.8,5.2,4.6,6.1,5.0,8.5,7.2,6.7]
    }

    df = pd.DataFrame(data)

    ranking = df.sort_values("risco",ascending=False)

    return ranking
