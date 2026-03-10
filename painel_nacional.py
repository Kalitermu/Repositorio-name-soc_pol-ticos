import pandas as pd

def dados_nacionais():

    dados = pd.DataFrame({
        "municipio":[
            "São Vicente",
            "Praia Grande",
            "Santos",
            "Guarujá",
            "Cubatão"
        ],
        "gasto_publico":[
            192000000000,
            282000000000,
            210000000000,
            98000000000,
            76000000000
        ],
        "risco":[
            7.2,
            6.5,
            4.8,
            5.1,
            4.2
        ]
    })

    return dados
