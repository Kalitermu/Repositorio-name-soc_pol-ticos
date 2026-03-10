import pandas as pd

def gerar_base_nacional():
    dados = pd.DataFrame({
        "cidade": [
            "São Vicente",
            "Praia Grande",
            "Santos",
            "Guarujá",
            "Cubatão",
            "Campinas",
            "São Paulo"
        ],
        "estado": [
            "SP","SP","SP","SP","SP","SP","SP"
        ],
        "gasto_total": [
            192069221173,
            282465538120,
            210000000000,
            98000000000,
            76000000000,
            300000000000,
            900000000000
        ],
        "desvio": [
            260529959,
            392609701,
            240000000,
            180000000,
            150000000,
            320000000,
            500000000
        ],
        "repeticoes": [
            8, 10, 6, 5, 4, 9, 12
        ],
        "concentracao": [
            0.37, 0.41, 0.29, 0.26, 0.24, 0.39, 0.44
        ],
        "lat": [
            -23.9631,
            -24.0058,
            -23.9608,
            -23.9933,
            -23.8911,
            -22.9056,
            -23.5505
        ],
        "lon": [
            -46.3919,
            -46.4028,
            -46.3336,
            -46.2564,
            -46.4253,
            -47.0608,
            -46.6333
        ]
    })

    dados["score_risco"] = (
        (dados["repeticoes"] / dados["repeticoes"].max()) * 3 +
        (dados["concentracao"] / dados["concentracao"].max()) * 4 +
        (dados["desvio"] / dados["desvio"].max()) * 3
    ).round(2)

    return dados.sort_values("score_risco", ascending=False)
