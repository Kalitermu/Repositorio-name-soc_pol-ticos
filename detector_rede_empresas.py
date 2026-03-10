import pandas as pd

def detectar_rede():

    dados = pd.DataFrame({
        "empresa":[
            "Construtora Alpha",
            "Construtora Alpha",
            "Construtora Beta",
            "Construtora Gamma",
            "Construtora Alpha",
            "Construtora Beta"
        ],
        "cidade":[
            "Santos",
            "São Vicente",
            "Praia Grande",
            "Guarujá",
            "Guarujá",
            "São Vicente"
        ],
        "valor":[
            8000000,
            6000000,
            3000000,
            2000000,
            5000000,
            4000000
        ]
    })

    agrupado = dados.groupby("empresa").agg({
        "cidade":"nunique",
        "valor":"sum"
    }).reset_index()

    suspeitas = agrupado[agrupado["cidade"] > 1]

    suspeitas = suspeitas.rename(columns={
        "cidade":"municipios",
        "valor":"valor_total"
    })

    return suspeitas
