import pandas as pd

def ranking():

    dados = pd.DataFrame({

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

        "risco":[
        8.5,
        7.2,
        6.9,
        6.1,
        5.8,
        5.6,
        4.9,
        4.4,
        4.2
        ]

    })

    return dados.sort_values("risco", ascending=False)
