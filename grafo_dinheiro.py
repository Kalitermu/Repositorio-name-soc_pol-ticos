
import networkx as nx
from pyvis.network import Network

def grafo_completo():

    dados = [
        ("Tesouro Nacional","Praia Grande"),
        ("Tesouro Nacional","Santos"),
        ("Tesouro Nacional","São Vicente"),

        ("Praia Grande","Construtora Alpha"),
        ("Santos","Construtora Alpha"),
        ("São Vicente","Tech Infra"),
        ("Guarujá","Serviços Delta"),

        ("Praia Grande","Benefícios Sociais"),
        ("Santos","Benefícios Sociais"),
        ("São Vicente","Benefícios Sociais")
    ]

    G = nx.Graph()

    for origem,destino in dados:
        G.add_edge(origem,destino)

    net = Network(height="600px",width="100%",bgcolor="#111",font_color="white")

    net.from_nx(G)

    arquivo = "grafo_dinheiro_publico.html"

    net.save_graph(arquivo)

    return arquivo
