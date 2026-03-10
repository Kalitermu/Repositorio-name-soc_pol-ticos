
import pandas as pd

def detectar_crescimento(df):

    if "valor_pago" not in df.columns:
        return pd.DataFrame()

    df = df.copy()

    df["crescimento"] = df["valor_pago"].pct_change()

    def alerta(x):
        if pd.isna(x):
            return "normal"
        if x > 0.3:
            return "🚨 crescimento alto"
        if x > 0.15:
            return "⚠ crescimento moderado"
        return "normal"

    df["alerta"] = df["crescimento"].apply(alerta)

    return df
