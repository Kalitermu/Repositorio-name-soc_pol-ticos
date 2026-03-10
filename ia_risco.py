
import pandas as pd

def prever_risco(df):

    media = df["valor"].mean()

    df["score_risco"] = df["valor"] / media

    df["nivel"] = "baixo"

    df.loc[df["score_risco"] > 1.5, "nivel"] = "médio"
    df.loc[df["score_risco"] > 3, "nivel"] = "alto"

    return df
