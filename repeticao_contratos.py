
import pandas as pd

def repeticao_por_orgao():

    data = {
        "orgao":[
            "Prefeitura Praia Grande",
            "Prefeitura Praia Grande",
            "Prefeitura Santos",
            "Prefeitura Santos",
            "Prefeitura Santos",
            "Prefeitura São Vicente",
            "Prefeitura São Vicente"
        ],
        "empresa":[
            "Construtora Alpha",
            "Construtora Alpha",
            "Tech Infra",
            "Construtora Alpha",
            "Tech Infra",
            "Serviços Delta",
            "Serviços Delta"
        ],
        "valor":[
            20000000,
            25000000,
            10000000,
            18000000,
            12000000,
            8000000,
            9000000
        ]
    }

    df = pd.DataFrame(data)

    contagem = df.groupby(["orgao","empresa"]).size().reset_index(name="contratos")

    contagem["risco"] = contagem["contratos"].apply(
        lambda x: "🚨 repetição alta" if x >= 3 else ("⚠ repetição moderada" if x == 2 else "normal")
    )

    return contagem
