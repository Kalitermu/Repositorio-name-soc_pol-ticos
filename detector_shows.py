import pandas as pd

def shows():

    df = pd.DataFrame({

        "cidade":[
        "São Paulo",
        "Guarulhos",
        "Santos",
        "Praia Grande",
        "Suzano"
        ],

        "evento":[
        "Show aniversario cidade",
        "Festival cultural",
        "Show verao",
        "Show virada ano",
        "Festa junina"
        ],

        "artista":[
        "Artista A",
        "Banda B",
        "Cantor C",
        "DJ D",
        "Dupla E"
        ],

        "valor":[
        1200000,
        850000,
        600000,
        950000,
        400000
        ]

    })

    media = df["valor"].mean()

    df["indice_risco"] = df["valor"] / media

    return df.sort_values("valor",ascending=False)
