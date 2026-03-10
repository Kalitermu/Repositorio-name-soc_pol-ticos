
import pandas as pd
import networkx as nx

def detectar_redes_suspeitas():

    dados = [
        ("Praia Grande","Construtora Alpha"),
        ("Praia Grande","Tech Infra"),
        ("Santos","Construtora Alpha"),
        ("São Vicente","Tech Infra"),
        ("Guarujá","Serviços Delta"),
        ("Cubatão","Serviços Delta"),
        ("Santos","Tech Infra"),
        ("São Vicente","Construtora Alpha")
    ]

    G = nx.Graph()
    for municipio, empresa in dados:
        G.add_edge(municipio, empresa)

    # centralidade de grau (quantas conexões cada nó tem)
    centralidade = nx.degree_centrality(G)

    registros = []
    for node, score in centralidade.items():
        # focar em empresas (não municípios)
        if node not in ["Praia Grande","Santos","São Vicente","Guarujá","Cubatão"]:
            nivel = "normal"
            if score > 0.5:
                nivel = "🚨 rede muito conectada"
            elif score > 0.3:
                nivel = "⚠ alta conectividade"

            registros.append({
                "empresa": node,
                "score_centralidade": round(score,3),
                "alerta": nivel
            })

    df = pd.DataFrame(registros).sort_values("score_centralidade", ascending=False)
    return df
