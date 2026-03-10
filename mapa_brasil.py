
import pandas as pd

def dados_brasil():

    data = {
        "cidade":[
        "São Vicente",
        "Santos",
        "Praia Grande",
        "Guarujá",
        "Cubatão",
        "São Paulo",
        "Rio de Janeiro",
        "Brasília"
        ],
        "lat":[
        -23.96,
        -23.96,
        -24.00,
        -23.99,
        -23.89,
        -23.55,
        -22.90,
        -15.79
        ],
        "lon":[
        -46.39,
        -46.33,
        -46.40,
        -46.25,
        -46.42,
        -46.63,
        -43.17,
        -47.88
        ],
        "risco":[7,5,4,6,5,8,7,6]
    }

    df = pd.DataFrame(data)

    return df
