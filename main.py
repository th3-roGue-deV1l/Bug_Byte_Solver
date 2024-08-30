import numpy as np
import networkx as nx
from pyvis.network import Network


nodes = ['17M', '3M', '49M', '75M', '60M', '29M', '79M', '39M', '25M', '54M', '31N', '19N23', '6N9N16', '8N', 'X1', 'X2', 'E1', 'E2']
edges = [('17M', '3M'), ('17M', '19N23'), ('3M', 'X1'), ('19N23', '54M'), ('54M', '60M'), ('60M', '79M'), ('79M', '39M'), ('79M', 'E1'), ('79M', '29M'), ('79M', '54M'), ('39M', 'X2'), ('X2', '25M'), ('25M', '29M'), ('31N', '54M'), ('75M', '49M'), ('49M', '8N'), ('49M', '60M'), ('49M', 'X1'), ('60M', '6N9N16'), ('75M', 'E2'), ('75M', '60M'), ('75M', '25M'), ('19N23', 'X1'), ('29M', '39M')]
weights = range(1, len(edges) + 1)

G = nx.Graph()

G.add_nodes_from(nodes)

for i, edge in enumerate(edges):
    G.add_edge(edge[0], edge[1], weight=weights[i])

#Draw the graph
net = Network(notebook=True, height="750px", width="100%", bgcolor="#222222", font_color="white",  cdn_resources="in_line")

# Convert NetworkX graph to Pyvis graph
# Convert NetworkX graph to Pyvis graph, transferring weights as edge labels
for node in G.nodes():
    net.add_node(node, label=str(node), title=f"Node {node}", color="darkblue", shape="circle", label_highlight_color="black")

for u, v, data in G.edges(data=True):
    weight = data['weight']
    net.add_edge(u, v, value=weight, title=f'Weight: {weight}', label=str(weight), color="lightblue", label_highlight_color="black")

# Enable physics for smooth motion
net.show_buttons(filter_=['physics'])
net.show("interactive_graph.html")

