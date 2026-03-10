
import pandas as pd

def distribuicao_por_area(df):

    # Espera colunas: _conta_ref, _valor_base
    if not {"_conta_ref","_valor_base"}.issubset(df.columns):
        return pd.DataFrame()

    # Mapeamento simples de contas → áreas (ajuste conforme sua base)
    mapa = {
        "3.3.90": "Serviços",
        "4.4.90": "Obras / Investimentos",
        "3.1.90": "Pessoal",
        "3.3.50": "Assistência Social",
        "3.3.30": "Saúde",
        "3.3.20": "Educação"
    }

    df = df.copy()
    df["area"] = df["_conta_ref"].astype(str).str[:5].map(mapa).fillna("Outros")

    resumo = (
        df.groupby("area")["_valor_base"]
        .sum()
        .reset_index()
        .sort_values("_valor_base", ascending=False)
    )

    return resumo
