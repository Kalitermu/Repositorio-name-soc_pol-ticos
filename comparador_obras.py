
import pandas as pd

def comparar_custos(df):

    if "tipo" not in df.columns or "valor" not in df.columns:
        return pd.DataFrame()

    medias = df.groupby("tipo")["valor"].mean().reset_index()

    df = df.merge(medias, on="tipo", suffixes=("", "_media"))

    df["alerta"] = df.apply(
        lambda x: "🚨 acima da média" if x["valor"] > x["valor_media"]*1.5 else "normal",
        axis=1
    )

    return df.sort_values("valor", ascending=False)
