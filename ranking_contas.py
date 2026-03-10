
import pandas as pd

def ranking_contas_suspeitas(df):

    if "_conta_ref" not in df.columns or "_valor_base" not in df.columns:
        return pd.DataFrame()

    grupo = df.groupby("_conta_ref")["_valor_base"].agg(
        total="sum",
        media="mean",
        repeticoes="count"
    ).reset_index()

    media_geral = grupo["media"].mean()

    grupo["score_risco"] = (
        (grupo["total"] / grupo["total"].max()) * 4 +
        (grupo["repeticoes"] / grupo["repeticoes"].max()) * 3 +
        (grupo["media"] / media_geral) * 3
    )

    grupo = grupo.sort_values(
        "score_risco",
        ascending=False
    )

    top10 = grupo.head(10)

    return top10
