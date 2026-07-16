# import networkx as nx
# from pyvis.network import Network
# import re
# from utils.weight_calculator import weightcalculator











# nodes = ['17M', '3M', '49M', '75M', '60M', '29M', '79M', '39M', '25M', '54M', '31N', '19N23', '6N9N16', '8N', 'X1', 'X2', 'E1', 'E2']
# edges = [('17M', '3M'), ('17M', '19N23'), ('3M', 'X1'), ('19N23', '54M'), ('54M', '60M'), ('60M', '79M'), ('79M', '39M'), ('79M', 'E1'), ('79M', '29M'), ('79M', '54M'), ('39M', 'X2'), ('X2', '25M'), ('25M', '29M'), ('31N', '54M'), ('75M', '49M'), ('49M', '8N'), ('49M', '60M'), ('49M', 'X1'), ('60M', '6N9N16'), ('75M', 'E2'), ('75M', '60M'), ('75M', '25M'), ('19N23', 'X1'), ('29M', '39M')]
# weights = range(1, len(edges) + 1)

# node_dict = {}
# i = 0
# j = 0
# k = 0
# l = 0
# for node in nodes:
#     if "M" in node:
#         node_dict['M' + str(i)] = node.strip('M')
#         i += 1
#     elif "N" in node:
#         node_dict['N' + str(j)] = node.strip('N')
#         j += 1
#     elif 'X' in node:
#         node_dict['X' + str(k)] = node.strip('X')
#         k += 1
#     elif 'E' in node:
#         node_dict['E' + str(l)] = node.strip('E')
#         l += 1
#     else:
#         node_dict['unkown'] = []
#         node_dict['unkown'].append(node.strip())
#         print("Unknown node found:", node)

# print(node_dict)
