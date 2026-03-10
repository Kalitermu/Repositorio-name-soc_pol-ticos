import pandas as pd

def dados():

    df = pd.DataFrame({

        "cidade":[
        "Guarulhos",
        "Itaquaquecetuba",
        "Suzano",
        "Santos",
        "Praia Grande"
        ],

        "obra":[
        "Pavimentação urbana",
        "Construção de escola",
        "Reforma de hospital",
        "Ampliação do porto",
        "Revitalização da orla"
        ],

        "empresa":[
        "Construtora Alpha",
        "Infra Brasil",
        "Construtora Alpha",
        "Porto Engenharia",
        "Litoral Obras"
        ],

        "valor":[
        12000000,
        8500000,
        20000000,
        45000000,
        7000000
        ],

        "lat":[
        -23.4543,
        -23.4861,
        -23.5425,
        -23.9608,
        -24.0058
        ],

        "lon":[
        -46.5333,
        -46.3486,
        -46.3108,
        -46.3336,
        -46.4028
        ]

    })

    return df
