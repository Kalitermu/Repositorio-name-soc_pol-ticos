import pandas as pd
from tesouro_api import buscar_dados_municipio
import contratos

def gerar_painel(codigo_ibge):

    df = buscar_dados_municipio(codigo_ibge)

    if df.empty:
        return None

    if "valor" in df.columns:
        valores = pd.to_numeric(df["valor"], errors="coerce")

    elif "valor_item" in df.columns:
        valores = pd.to_numeric(df["valor_item"], errors="coerce")

    else:
        return None

    valores = valores.dropna()

    total = valores.sum()
    media = valores.mean()
    desvio = valores.std()

    repeticoes = valores.duplicated().sum()

    score = 0

    if desvio > media:
        score += 3

    if repeticoes > 5:
        score += 2

    if valores.max() > media * 5:
        score += 4

    contratos_df = contratos.empresas_suspeitas()

    return {
        "total":total,
        "media":media,
        "desvio":desvio,
        "repeticoes":repeticoes,
        "score":score,
        "contratos":contratos_df
    }
