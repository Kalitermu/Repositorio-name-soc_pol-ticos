
import pandas as pd

def alerta_risco(df):

    if "score" not in df.columns:
        return ""

    df = df.sort_values("ano")

    if len(df) < 2:
        return ""

    ultimo = df["score"].iloc[-1]
    anterior = df["score"].iloc[-2]

    if ultimo > anterior:
        return "⚠ risco fiscal aumentou"
    elif ultimo < anterior:
        return "🟢 risco fiscal diminuiu"
    else:
        return "➖ risco estável"
