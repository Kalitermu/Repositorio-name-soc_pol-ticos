
import pandas as pd

def detectar_picos(df_tempo):

    if df_tempo is None or df_tempo.empty:
        return pd.DataFrame()

    media = df_tempo["_valor_base"].mean()
    desvio = df_tempo["_valor_base"].std()

    df_tempo["alerta"] = df_tempo["_valor_base"].apply(
        lambda x: "🚨 pico anormal" if x > media + 2*desvio else "normal"
    )

    return df_tempo
