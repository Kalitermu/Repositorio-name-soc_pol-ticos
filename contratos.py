import pandas as pd

def empresas_suspeitas():

    dados = pd.DataFrame({
        "empresa":[
            "Construtora Norberto Odebrecht",
            "Andrade Gutierrez",
            "Camargo Corrêa",
            "Queiroz Galvão",
            "OAS Engenharia",
            "Andrade Gutierrez",
            "Camargo Corrêa"
        ],
        "valor":[
            250000000,
            180000000,
            120000000,
            90000000,
            85000000,
            60000000,
            40000000
        ]
    })

    ranking = dados.groupby("empresa")["valor"].sum().reset_index()

    ranking = ranking.rename(columns={"valor":"valor_total"})

    ranking = ranking.sort_values("valor_total",ascending=False)

    media = ranking["valor_total"].mean()

    def risco(valor):

        if valor > media * 2:
            return "⚠ alta concentração"

        elif valor > media:
            return "🟡 atenção"

        else:
            return "normal"

    ranking["risco"] = ranking["valor_total"].apply(risco)

    return ranking
