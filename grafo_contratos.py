
import networkx as nx
from pyvis.network import Network

def gerar_grafo():

    dados = [
        ("Praia Grande","Construtora Alpha"),
        ("Praia Grande","Tech Infra"),
        ("Santos","Construtora Alpha"),
        ("São Vicente","Tech Infra"),
        ("Guarujá","Serviços Delta"),
        ("Cubatão","Serviços Delta")
    ]

    G = nx.Graph()

    for municipio,empresa in dados:
        G.add_node(municipio, tipo="municipio")
        G.add_node(empresa, tipo="empresa")
        G.add_edge(municipio,empresa)

    net = Network(height="500px", width="100%", bgcolor="#111", font_color="white")

    net.from_nx(G)

    arquivo = "grafo_contratos.html"

    net.save_graph(arquivo)

    return arquivo
