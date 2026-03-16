import pandas as pd
import contratos


def gerar_painel(codigo_ibge):

    # buscar contratos
    df = contratos.buscar_contratos()

    if df.empty:

        return {
            "cidade": codigo_ibge,
            "total_contratos": 0,
            "valor_total": 0,
            "top_empresas": pd.DataFrame(),
            "contratos": pd.DataFrame()
        }

    # total contratos
    total_contratos = len(df)

    # valor total
    valor_total = df["valor"].sum()

    # ranking empresas
    ranking = (
        df.groupby("empresa")["valor"]
        .sum()
        .reset_index()
        .sort_values("valor", ascending=False)
        .head(10)
    )

    return {
        "cidade": codigo_ibge,
        "total_contratos": total_contratos,
        "valor_total": valor_total,
        "top_empresas": ranking,
        "contratos": df
    }
