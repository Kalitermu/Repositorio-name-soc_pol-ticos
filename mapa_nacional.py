import pandas as pd

def dados_municipios():

    dados = pd.DataFrame({
        "municipio":[
            "São Paulo",
            "Rio de Janeiro",
            "Belo Horizonte",
            "Salvador",
            "Curitiba",
            "Porto Alegre",
            "Recife"
        ],
        "lat":[
            -23.55,
            -22.90,
            -19.92,
            -12.97,
            -25.43,
            -30.03,
            -8.05
        ],
        "lon":[
            -46.63,
            -43.20,
            -43.94,
            -38.50,
            -49.27,
            -51.23,
            -34.88
        ],
        "score":[
            8.5,
            7.9,
            6.2,
            7.1,
            5.8,
            4.9,
            6.5
        ]
    })

    return dados
