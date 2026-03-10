import pandas as pd
import base_contratos

def buscar_empresa(nome):
    df = base_contratos.carregar_base()

    if not nome.strip():
        return df

    filtro = df["empresa"].str.contains(nome, case=False, na=False)
    return df[filtro].sort_values("valor", ascending=False)

def ranking_empresas():
    df = base_contratos.carregar_base()

    ranking = df.groupby("empresa", as_index=False).agg(
        qtd_contratos=("empresa", "count"),
        valor_total=("valor", "sum")
    )

    return ranking.sort_values("valor_total", ascending=False)
