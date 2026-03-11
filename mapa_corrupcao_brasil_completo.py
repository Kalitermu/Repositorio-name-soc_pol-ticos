import pandas as pd

def gerar_dados():

    dados = [
        {"cidade":"São Paulo","lat":-23.55,"lon":-46.63,"score":9.1},
        {"cidade":"Guarulhos","lat":-23.45,"lon":-46.53,"score":7.5},
        {"cidade":"Itaquaquecetuba","lat":-23.48,"lon":-46.34,"score":6.8},
        {"cidade":"Suzano","lat":-23.54,"lon":-46.31,"score":6.2},
        {"cidade":"Poá","lat":-23.52,"lon":-46.34,"score":5.9},
        {"cidade":"Ferraz de Vasconcelos","lat":-23.54,"lon":-46.37,"score":5.6},
        {"cidade":"Santos","lat":-23.96,"lon":-46.33,"score":4.7},
        {"cidade":"Praia Grande","lat":-24.00,"lon":-46.41,"score":4.3},
        {"cidade":"São Vicente","lat":-23.96,"lon":-46.38,"score":4.1}
    ]

    df = pd.DataFrame(dados)

    # gerar alerta automaticamente
    def definir_alerta(score):
        if score > 8:
            return "alto"
        elif score > 5:
            return "medio"
        else:
            return "baixo"

    df["alerta"] = df["score"].apply(definir_alerta)

    return df
