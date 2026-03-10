
import pandas as pd

def distribuicao_secretarias(df):

    if "_conta_ref" not in df.columns or "_valor_base" not in df.columns:
        return pd.DataFrame()

    mapa_secretaria = {
        "10":"Saúde",
        "12":"Educação",
        "15":"Obras",
        "04":"Administração"
    }

    df = df.copy()

    df["secretaria"] = df["_conta_ref"].astype(str).str[:2].map(mapa_secretaria)

    df["secretaria"] = df["secretaria"].fillna("Outras")

    resumo = (
        df.groupby("secretaria")["_valor_base"]
        .sum()
        .reset_index()
        .sort_values("_valor_base",ascending=False)
    )

    return resumo
