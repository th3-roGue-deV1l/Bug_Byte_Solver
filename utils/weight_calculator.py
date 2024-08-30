import networkx as nx
import re
import random

#Checks node type
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

#Assigns node type
def assign_node(G, nodes):
    for node in nodes:
        G.nodes[node]['type'] = node_type(node)

# Recursive function
# Until weight >= weight in node 'N'
def Nrecurse(G, node, total_weight = 0, count = 0, weight_check = [], initial_node = None):
    ###
    # node: currently examining this node
    # total_weight: total weight of the previous nodes
    # count: number of times the function has been called
    ###

    # List of edges in the current node
    edges = []
    r =[]
    for p, q, data in G.edges(node, data=True):
        edges.append((p, q, data))
    r = random.choice([p if p != node else q if q != initial_node else None for p, q, data in edges])

    #Adding the weight of an edge
    for p, q, data in G.edges(node, data=True):
        if p == r or q == r:
            total_weight += data['weight']
            break

    #Checking if the weightsum exceeds the node number
    for num in weight_check:
        if total_weight == num:
            weight_check.remove(num)
            G.nodes[initial_node]['weight'].append(total_weight)
            return G.nodes[initial_node]['weight'] if weight_check == [] else Nrecurse(G=G, node=initial_node, count=count, weight_check=weight_check, initial_node=initial_node)
        if total_weight > num:
    #         # it is default num for now, need to make it go back later.
            G.nodes[initial_node]['weight'].append(num)
            weight_check.remove(num)
            return G.nodes[initial_node]['weight'] if weight_check == [] else Nrecurse(G=G, node=initial_node, count=count, weight_check=weight_check, initial_node=initial_node)
        
    if count > 100:
        print('limit exceeded !!!')
        return G.nodes[initial_node]['weight']
    count += 1
    return Nrecurse(G, r, total_weight, count, weight_check, initial_node)
    # print(edges)
    return 1
    

def weightcalculator(G, nodes, edges):
    #Adding nodes
    assign_node(G, nodes)

    #MWeight Adder
    for u in G.nodes():
        if G.nodes[u]['type'] == 'M':
            #Initialising the weight list
            G.nodes[u]['weight'] = []
            total_weight = 0
            #Total weight of the node
            for p, q, data in G.edges(u, data=True):
                total_weight += data['weight']
            G.nodes[u]['weight'] = total_weight

    #NWeight Adder
    for v in G.nodes():
        if G.nodes[v]['type'] == 'N':
            #Initialising the weight list
            G.nodes[v]['weight'] = []

            # List of weights in the node 'N'
            try:
                weight_check = list(map(int, v.split('N')))
            except ValueError:
                vtemp = v.split('N')
                vtemp = [item for item in vtemp if item]
                weight_check = list(map(int, vtemp))

            #Recursing for a single node 'N'
            Nrecurse(G, node=v, weight_check=weight_check, initial_node=v)