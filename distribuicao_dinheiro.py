
import pandas as pd

def distribuicao_dinheiro():

    data = {
        "categoria":[
            "Saúde",
            "Educação",
            "Infraestrutura",
            "Contratos públicos",
            "Programas sociais"
        ],
        "valor":[
            45000000000,
            38000000000,
            52000000000,
            60000000000,
            9000000000
        ]
    }

    df = pd.DataFrame(data)

    return df
