import pandas as pd

def painel_inteligencia():

    dados = pd.DataFrame({
        "cidade":[
            "São Paulo",
            "Santos",
            "Praia Grande",
            "São Vicente",
            "Guarujá",
            "Cubatão"
        ],
        "risco_fiscal":[8,6,5,7,4,6],
        "superfaturamento":[7,4,3,6,2,5],
        "cartel_empresas":[6,3,2,7,2,4],
        "pressao_social":[5,4,3,6,3,4],
        "concentracao_contratos":[8,5,4,7,3,5]
    })

    dados["score_total"] = (
        dados["risco_fiscal"] * 0.25 +
        dados["superfaturamento"] * 0.25 +
        dados["cartel_empresas"] * 0.20 +
        dados["pressao_social"] * 0.15 +
        dados["concentracao_contratos"] * 0.15
    ).round(2)

    def classificar(score):
        if score >= 7:
            return "🚨 alto risco"
        elif score >= 4:
            return "🟡 médio risco"
        return "🟢 baixo risco"

    dados["alerta"] = dados["score_total"].apply(classificar)

    return dados.sort_values("score_total", ascending=False)
