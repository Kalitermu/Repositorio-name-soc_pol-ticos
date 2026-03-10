import pandas as pd

def detectar_cartel():

    dados = pd.DataFrame({
        "empresa":[
            "Construtora Alpha",
            "Construtora Alpha",
            "Construtora Beta",
            "Infra Brasil",
            "Infra Brasil",
            "Infra Brasil"
        ],
        "cidade":[
            "Santos",
            "São Vicente",
            "Praia Grande",
            "Santos",
            "Praia Grande",
            "Guarujá"
        ],
        "valor":[
            5000000,
            7000000,
            3000000,
            4000000,
            4500000,
            4200000
        ]
    })

    resumo = dados.groupby("empresa").agg({
        "cidade":"nunique",
        "valor":"sum"
    }).reset_index()

    suspeitos = resumo[resumo["cidade"] > 1]

    suspeitos = suspeitos.rename(columns={
        "cidade":"cidades",
        "valor":"valor_total"
    })

    return suspeitos
