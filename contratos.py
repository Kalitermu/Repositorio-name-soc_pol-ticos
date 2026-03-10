import pandas as pd
import pncp_api

def empresas_suspeitas():

    df = pncp_api.buscar_contratos()

    if df.empty:
        return pd.DataFrame()

    ranking = df.groupby("empresa")["valor"].sum().reset_index()

    ranking = ranking.rename(columns={"valor":"valor_total"})

    ranking = ranking.sort_values("valor_total",ascending=False)

    media = ranking["valor_total"].mean()

    def risco(valor):

        if valor > media * 2:
            return "⚠ concentração alta"

        elif valor > media:
            return "🟡 atenção"

        else:
            return "normal"

    ranking["risco"] = ranking["valor_total"].apply(risco)

    return ranking
