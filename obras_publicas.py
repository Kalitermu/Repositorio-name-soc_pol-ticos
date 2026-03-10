import pandas as pd

def carregar_obras():

    dados = pd.DataFrame({
        "obra":[
            "Reforma de escola",
            "Construção de UBS",
            "Pavimentação de avenida",
            "Ampliação de hospital"
        ],
        "empresa":[
            "Construtora Alpha",
            "Infra Brasil",
            "Construtora Beta",
            "Engenharia Brasil"
        ],
        "valor":[
            5000000,
            7200000,
            3500000,
            9000000
        ],
        "lat":[
            -23.96,
            -24.00,
            -23.95,
            -23.98
        ],
        "lon":[
            -46.38,
            -46.41,
            -46.33,
            -46.36
        ]
    })

    return dados
