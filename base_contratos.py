import pandas as pd
import pncp_api

def carregar_base():
    df = pncp_api.buscar_contratos()

    if df.empty:
        return pd.DataFrame({
            "orgao": ["Prefeitura de Santos", "Prefeitura de São Vicente", "Prefeitura de Praia Grande"],
            "empresa": ["Construtora Alpha", "Infra Brasil", "Construtora Alpha"],
            "valor": [2500000, 4100000, 3800000],
            "modalidade": ["Pregão", "Concorrência", "Pregão"],
            "data": ["2026-03-01", "2026-03-02", "2026-03-03"]
        })

    df["valor"] = pd.to_numeric(df["valor"], errors="coerce").fillna(0)
    df["empresa"] = df["empresa"].fillna("Não informado")
    df["orgao"] = df["orgao"].fillna("Não informado")
    df["modalidade"] = df["modalidade"].fillna("Não informado")
    df["data"] = df["data"].fillna("")
    return df
