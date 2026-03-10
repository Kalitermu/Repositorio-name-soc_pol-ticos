import pandas as pd
import base_contratos

def detectar():

    df = base_contratos.carregar_base()

    if df.empty:
        return pd.DataFrame()

    resumo = df.groupby("empresa", as_index=False).agg(
        qtd_contratos=("empresa", "count"),
        valor_total=("valor", "sum"),
        qtd_orgaos=("orgao", "nunique")
    )

    media_valor = resumo["valor_total"].mean() if not resumo.empty else 0

    def classificar(row):
        score = 0

        if row["qtd_orgaos"] >= 2:
            score += 2
        if row["qtd_contratos"] >= 3:
            score += 2
        if media_valor > 0 and row["valor_total"] > media_valor * 2:
            score += 3

        if score >= 5:
            return "🚨 alto risco"
        elif score >= 3:
            return "🟡 atenção"
        return "normal"

    resumo["alerta"] = resumo.apply(classificar, axis=1)

    return resumo.sort_values(
        ["alerta", "valor_total", "qtd_contratos"],
        ascending=[False, False, False]
    )
