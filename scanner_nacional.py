import pandas as pd
from tesouro_api import buscar_dados_municipio
import contratos

CIDADES = {
    "São Paulo": "3550308",
    "Santos": "3548500",
    "Praia Grande": "3541000",
    "São Vicente": "3551009",
    "Guarujá": "3518701",
    "Cubatão": "3513504"
}

COORDS = {
    "São Paulo": (-23.55, -46.63),
    "Santos": (-23.95, -46.33),
    "Praia Grande": (-24.00, -46.41),
    "São Vicente": (-23.96, -46.38),
    "Guarujá": (-23.99, -46.25),
    "Cubatão": (-23.89, -46.42)
}

def _valor_series(df: pd.DataFrame) -> pd.Series:
    if df.empty:
        return pd.Series(dtype="float64")
    if "valor" in df.columns:
        s = pd.to_numeric(df["valor"], errors="coerce")
    elif "valor_item" in df.columns:
        s = pd.to_numeric(df["valor_item"], errors="coerce")
    else:
        return pd.Series(dtype="float64")
    return s.dropna()

def score_fiscal(df: pd.DataFrame) -> dict:
    valores = _valor_series(df)
    if valores.empty:
        return {
            "total": 0.0,
            "media": 0.0,
            "desvio": 0.0,
            "repeticoes": 0,
            "maximo": 0.0,
            "score_fiscal": 0.0
        }

    total = float(valores.sum())
    media = float(valores.mean())
    desvio = float(valores.std() if len(valores) > 1 else 0.0)
    repeticoes = int(valores.duplicated().sum())
    maximo = float(valores.max())

    score = 0.0
    if media > 0 and desvio > media:
        score += 3
    if repeticoes > 10:
        score += 2
    if media > 0 and maximo > media * 5:
        score += 3
    if total > 0 and media > 0 and total > media * 100:
        score += 2

    return {
        "total": total,
        "media": media,
        "desvio": desvio,
        "repeticoes": repeticoes,
        "maximo": maximo,
        "score_fiscal": round(score, 2)
    }

def score_contratos() -> pd.DataFrame:
    df = contratos.empresas_suspeitas()
    if df.empty or "valor_total" not in df.columns:
        return pd.DataFrame(columns=["empresa", "valor_total", "score_contrato"])

    media = df["valor_total"].mean()
    df = df.copy()
    df["score_contrato"] = 0.0
    df.loc[df["valor_total"] > media, "score_contrato"] = 1.5
    df.loc[df["valor_total"] > media * 2, "score_contrato"] = 3.0
    return df

def executar_scanner() -> pd.DataFrame:
    contratos_df = score_contratos()
    score_contratos_global = float(contratos_df["score_contrato"].max()) if not contratos_df.empty else 0.0

    saida = []
    for cidade, codigo in CIDADES.items():
        df = buscar_dados_municipio(codigo)
        fiscal = score_fiscal(df)
        lat, lon = COORDS[cidade]

        score_total = round(
            fiscal["score_fiscal"] * 0.7 + score_contratos_global * 0.3,
            2
        )

        if score_total >= 7:
            alerta = "🚨 alto risco"
        elif score_total >= 4:
            alerta = "🟡 médio risco"
        else:
            alerta = "🟢 baixo risco"

        saida.append({
            "cidade": cidade,
            "codigo_ibge": codigo,
            "lat": lat,
            "lon": lon,
            "total": fiscal["total"],
            "media": fiscal["media"],
            "desvio": fiscal["desvio"],
            "repeticoes": fiscal["repeticoes"],
            "score_fiscal": fiscal["score_fiscal"],
            "score_total": score_total,
            "alerta": alerta
        })

    return pd.DataFrame(saida).sort_values("score_total", ascending=False)
