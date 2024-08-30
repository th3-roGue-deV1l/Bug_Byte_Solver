import networkx as nx
from main import G, nodes, edges

def node_type(node):
    if 'M' in node:
        return 'M'
    elif 'N' in node:
        return 'N'
    elif 'X' in node:
        return 'X'
    elif 'E' in node:
        return 'E'
    else:
        return 'U'

def assign_node(G, nodes):
    for node in nodes:
        G.nodes[node]['type'] = node_type(node)


def weightcalculator(G, nodes, edges):
    if not G:
        G = nx.Graph()
        G.add_nodes_from(nodes)
        for i, edge in enumerate(edges):
            G.add_edge(edge[0], edge[1], weight=i+1)
        assign_node(G, nodes)
    assign_node(G, nodes)
    weights = {}
    for u in G.nodes():
        if G.nodes[u]['type'] == 'M':
            total_weight = 0
            for e in G.edges(u, data=True):
                total_weight += e[2]['weight']
            weights[u] = total_weight
    print(weights)
weightcalculator(G, nodes, edges)
