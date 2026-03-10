import pandas as pd

def dados():

    df = pd.DataFrame({

        "cidade":[
        "São Paulo",
        "Guarulhos",
        "Itaquaquecetuba",
        "Suzano",
        "Poá",
        "Ferraz de Vasconcelos",
        "Santos",
        "Praia Grande",
        "São Vicente"
        ],

        "lat":[
        -23.55,
        -23.45,
        -23.48,
        -23.54,
        -23.52,
        -23.54,
        -23.96,
        -24.00,
        -23.96
        ],

        "lon":[
        -46.63,
        -46.53,
        -46.34,
        -46.31,
        -46.34,
        -46.37,
        -46.33,
        -46.41,
        -46.38
        ],

        "risco":[
        9.1,
        7.5,
        6.8,
        6.2,
        5.9,
        5.6,
        4.7,
        4.3,
        4.1
        ]

    })

    return df

def dados_mapa():
    return dados()

