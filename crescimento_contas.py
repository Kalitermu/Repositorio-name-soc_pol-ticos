
import pandas as pd

def crescimento_por_conta(df):

    # Espera colunas: _conta_ref, _valor_base, ano
    if not {"_conta_ref","_valor_base","ano"}.issubset(df.columns):
        return pd.DataFrame()

    grupo = (
        df.groupby(["_conta_ref","ano"])["_valor_base"]
        .sum()
        .reset_index()
        .sort_values(["_conta_ref","ano"])
    )

    grupo["crescimento"] = (
        grupo.groupby("_conta_ref")["_valor_base"]
        .pct_change()
    )

    # Classificação de risco
    def classificar(x):
        if pd.isna(x):
            return "—"
        if x > 1.0:
            return "🚨 >100%"
        elif x > 0.5:
            return "⚠ 50–100%"
        elif x > 0.2:
            return "atenção"
        else:
            return "normal"

    grupo["risco"] = grupo["crescimento"].apply(classificar)

    # Pegar últimos anos por conta
    ultimos = (
        grupo.sort_values("ano")
        .groupby("_conta_ref")
        .tail(1)
        .sort_values("crescimento", ascending=False)
    )

    return ultimos
