
import pandas as pd

def alertas_areas(df):

    alertas = []

    for _,row in df.iterrows():

        if row["obras"] > row["saude"] * 1.5:
            alertas.append(
                f"⚠ {row['municipio']} investe muito mais em obras que em saúde"
            )

        if row["social"] < row["total"] * 0.02:
            alertas.append(
                f"🚨 {row['municipio']} tem baixo investimento social"
            )

    return alertas
