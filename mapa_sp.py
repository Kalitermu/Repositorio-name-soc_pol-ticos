import pandas as pd

def dados_mapa():

    dados = pd.DataFrame({
        "cidade":[
            "Guarulhos",
            "Itaquaquecetuba",
            "Arujá",
            "Suzano",
            "Poá",
            "Ferraz de Vasconcelos",
            "Santos",
            "Praia Grande",
            "São Vicente"
        ],
        "lat":[
            -23.4543,
            -23.4861,
            -23.3967,
            -23.5425,
            -23.5280,
            -23.5408,
            -23.9608,
            -24.0058,
            -23.9631
        ],
        "lon":[
            -46.5333,
            -46.3486,
            -46.3200,
            -46.3108,
            -46.3447,
            -46.3687,
            -46.3336,
            -46.4028,
            -46.3919
        ],
        "risco":[
            7,
            6,
            5,
            6,
            4,
            5,
            4,
            3,
            4
        ]
    })

    return dados
