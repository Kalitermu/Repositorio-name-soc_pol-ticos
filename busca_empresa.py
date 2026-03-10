
import pandas as pd

def buscar_empresa(nome):

    data = {
        "empresa":[
            "Construtora Alpha",
            "Construtora Alpha",
            "Tech Infra",
            "Tech Infra",
            "Serviços Delta"
        ],
        "cidade":[
            "Praia Grande",
            "Santos",
            "São Vicente",
            "Santos",
            "Guarujá"
        ],
        "valor":[
            200000000,
            150000000,
            80000000,
            120000000,
            50000000
        ]
    }

    df = pd.DataFrame(data)

    resultado = df[df["empresa"].str.contains(nome, case=False)]

    if resultado.empty:
        return None, None

    resumo = {
        "contratos": len(resultado),
        "valor_total": resultado["valor"].sum(),
        "cidades": resultado["cidade"].nunique()
    }

    return resultado, resumo
