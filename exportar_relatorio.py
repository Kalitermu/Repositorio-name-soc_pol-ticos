
import pandas as pd

def gerar_relatorio(df):

    if df is None or df.empty:
        return None

    arquivo = "relatorio_radar_transparencia.csv"

    df.to_csv(arquivo,index=False)

    return arquivo
