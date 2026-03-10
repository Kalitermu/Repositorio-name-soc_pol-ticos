
import pandas as pd

def dados_integrados():
    data = {
        "municipio": [
            "Praia Grande",
            "Santos",
            "São Vicente",
            "Guarujá",
            "Cubatão"
        ],
        "lat": [-24.0058, -23.9608, -23.9631, -23.9938, -23.8911],
        "lon": [-46.4028, -46.3336, -46.3919, -46.2564, -46.4253],
        "gasto_publico": [
            261559209186,
            120000000000,
            192069221173,
            50000000000,
            40000000000
        ],
        "contratos": [85, 70, 66, 40, 32],
        "beneficios_sociais": [
            9000000,
            12000000,
            11000000,
            8000000,
            7000000
        ]
    }

    df = pd.DataFrame(data)

    df["indice_social"] = df["beneficios_sociais"] / df["gasto_publico"]
    df["score_integrado"] = (
        (df["gasto_publico"] / df["gasto_publico"].max()) * 0.5 +
        (df["contratos"] / df["contratos"].max()) * 0.3 +
        (1 - (df["indice_social"] / df["indice_social"].max())) * 0.2
    )

    df["raio"] = (df["gasto_publico"] / 10000000).astype(int)

    return df
