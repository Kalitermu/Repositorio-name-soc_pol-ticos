import pandas as pd

def empresas_suspeitas():

    dados = pd.DataFrame({
        "empresa":[
            "Construtora Alpha",
            "Construtora Beta",
            "Engenharia Brasil",
            "Obras Litoral",
            "Construtora Alpha",
            "Construtora Alpha"
        ],
        "valor":[
            5000000,
            7000000,
            3000000,
            2500000,
            8000000,
            9000000
        ]
    })

    ranking = dados.groupby("empresa")["valor"].sum().reset_index()

    ranking = ranking.rename(columns={"valor":"valor_total"})

    ranking = ranking.sort_values("valor_total",ascending=False)

    # detectar concentração de contratos
    media = ranking["valor_total"].mean()

    def risco(valor):

        if valor > media * 2:
            return "⚠ suspeito"

        elif valor > media:
            return "🟡 atenção"

        else:
            return "normal"

    ranking["risco"] = ranking["valor_total"].apply(risco)

    return ranking
