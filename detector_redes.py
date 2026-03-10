
import pandas as pd
import networkx as nx
from networkx.algorithms import community

def detectar_redes_suspeitas():

    dados = [
        ("Praia Grande","Construtora Alpha"),
        ("Praia Grande","Tech Infra"),
        ("Santos","Construtora Alpha"),
        ("São Vicente","Tech Infra"),
        ("Guarujá","Serviços Delta"),
        ("Cubatão","Serviços Delta"),
        ("Santos","Tech Infra"),
        ("São Vicente","Construtora Alpha"),
        ("Praia Grande","Serviços Delta")
    ]

    G = nx.Graph()

    for municipio,empresa in dados:
        G.add_edge(municipio,empresa)

    # centralidade (quem está mais conectado)
    centralidade = nx.degree_centrality(G)

    registros = []
    municipios = ["Praia Grande","Santos","São Vicente","Guarujá","Cubatão"]

    for node,score in centralidade.items():

        if node not in municipios:

            alerta = "normal"

            if score > 0.5:
                alerta = "🚨 alta centralidade"
            elif score > 0.3:
                alerta = "⚠ empresa muito conectada"

            registros.append({
                "empresa":node,
                "score_centralidade":round(score,3),
                "alerta":alerta
            })

    df_empresas = pd.DataFrame(registros).sort_values("score_centralidade",ascending=False)

    # detectar clusters
    comunidades = community.greedy_modularity_communities(G)

    clusters = []

    for i,grupo in enumerate(comunidades):
        clusters.append({
            "cluster":i+1,
            "nodos":", ".join(list(grupo))
        })

    df_clusters = pd.DataFrame(clusters)

    return df_empresas, df_clusters
