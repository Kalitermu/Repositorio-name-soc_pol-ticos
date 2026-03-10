import pandas as pd
import networkx as nx

def gerar_rede(df):

    G=nx.Graph()

    for _,row in df.iterrows():

        cidade=row["orgao"]
        empresa=row["empresa"]

        G.add_node(cidade,type="orgao")
        G.add_node(empresa,type="empresa")

        G.add_edge(cidade,empresa)

    return G
