import pandas as pd

def dados_mapa():

    dados = pd.DataFrame({
        "cidade":[
            "São Paulo",
            "Santos",
            "Praia Grande",
            "São Vicente",
            "Guarujá",
            "Cubatão"
        ],
        "lat":[
            -23.55,
            -23.95,
            -24.00,
            -23.96,
            -23.99,
            -23.89
        ],
        "lon":[
            -46.63,
            -46.33,
            -46.41,
            -46.38,
            -46.26,
            -46.42
        ],
        "risco":[
            8,
            6,
            5,
            7,
            4,
            6
        ]
    })

    return dados
