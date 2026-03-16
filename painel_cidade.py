import pandas as pd


def gerar_painel(codigo_ibge):

    # exemplo de dados simulados
    contratos = pd.DataFrame({
        "empresa": [
            "Engenharia Brasil",
            "Construtora Alpha",
            "InfraTech",
            "Obras Unidas"
        ],
        "valor": [
            1200000,
            850000,
            420000,
            310000
        ]
    })

    # total de contratos
    total_contratos = len(contratos)

    # valor total
    valor_total = contratos["valor"].sum()

    # ranking empresas
    top_empresas = contratos.sort_values(
        by="valor",
        ascending=False
    )

    return {
        "codigo": codigo_ibge,
        "total_contratos": total_contratos,
        "valor_total": valor_total,
        "top_empresas": top_empresas,
        "contratos": contratos
    }
