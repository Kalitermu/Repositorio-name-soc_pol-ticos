
import pandas as pd

def dados_sociais():

    data = {
        "cidade":[
        "São Vicente",
        "Santos",
        "Praia Grande",
        "Guarujá",
        "Cubatão"
        ],
        "beneficiarios":[
        45000,
        20000,
        15000,
        22000,
        18000
        ],
        "valor_beneficio":[
        27000000,
        12000000,
        9000000,
        13000000,
        10000000
        ]
    }

    df = pd.DataFrame(data)

    return df
