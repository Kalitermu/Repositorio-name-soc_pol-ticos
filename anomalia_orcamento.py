
import pandas as pd

def detectar_anomalia(df):

    alertas = []

    cidades = df.columns[1:]

    for cidade in cidades:

        valores = df[cidade].pct_change()

        if valores.max() > 0.5:
            alertas.append(
                f"🚨 Crescimento anormal detectado em {cidade}"
            )

    return alertas
