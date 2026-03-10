import pandas as pd
import tesouro_api
import contratos
import detector_corrupcao

def analisar_cidade(codigo_ibge):

    df=tesouro_api.buscar_dados_municipio(codigo_ibge)

    if df.empty:
        return None

    if "valor" in df.columns:
        df["valor_calc"]=pd.to_numeric(df["valor"],errors="coerce")

    elif "valor_item" in df.columns:
        df["valor_calc"]=pd.to_numeric(df["valor_item"],errors="coerce")

    df=df.dropna(subset=["valor_calc"])

    media=df["valor_calc"].mean()

    picos=df[df["valor_calc"]>media*2]

    repetidos=df[df["valor_calc"].duplicated()]

    contratos_df=contratos.empresas_suspeitas()

    return {
        "picos":picos,
        "repetidos":repetidos,
        "contratos":contratos_df
    }
