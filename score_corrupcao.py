import pandas as pd

def calcular_score(df):

    if df.empty:
        return 0

    valores = pd.to_numeric(df["valor_calc"], errors="coerce").dropna()

    total = valores.sum()
    media = valores.mean()
    desvio = valores.std()

    repeticoes = valores.duplicated().sum()

    score = 0

    if desvio > media:
        score += 3

    if repeticoes > 5:
        score += 2

    if total > media * 100:
        score += 5

    return score
