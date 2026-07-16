import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes with constraints
G.add_node("M1", constraint=54)  # Node M with sum constraint
G.add_node("M2", constraint=60)
G.add_node("M3", constraint=75)
G.add_node("N1", path_sum=79)

# Add edges (weights will be assigned later)
edges = [
    ("M1", "N1"), ("M1", "M2"), ("M2", "M3"),
    ("M2", "N1"), ("M3", "N1")
]
G.add_edges_from(edges)

# Visualize the graph
nx.draw(G, with_labels=True, node_color='lightblue')





# from ortools.sat.python import cp_model

# def solve_graph_puzzle(G):
#     model = cp_model.CpModel()
#     edge_weights = {}

#     # Assign variables to each edge
#     for u, v in G.edges:
#         edge_weights[(u, v)] = model.NewIntVar(1, 24, f"weight_{u}_{v}")

#     # Ensure all weights are unique
#     model.AddAllDifferent(edge_weights.values())

#     # Add constraints for labeled nodes
#     for node, data in G.nodes(data=True):
#         if 'constraint' in data:
#             model.Add(
#                 sum(edge_weights[(min(node, n), max(node, n))]
#                     for n in G.neighbors(node)) == data['constraint']
#             )

#     # Solve the model
#     solver = cp_model.CpSolver()
#     status = solver.Solve(model)

#     if status == cp_model.OPTIMAL:
#         return {k: solver.Value(v) for k, v in edge_weights.items()}
#     else:
#         return None

# # Example usage
# result = solve_graph_puzzle(G)
# print(result)





# def find_shortest_path(G, weights, start, end):
#     # Assign the solved weights to the graph
#     for (u, v), weight in weights.items():
#         G[u][v]['weight'] = weight

#     # Find the shortest path
#     path = nx.shortest_path(G, source=start, target=end, weight='weight')

#     # Extract weights from the path
#     path_weights = [
#         G[path[i]][path[i+1]]['weight'] for i in range(len(path)-1)
#     ]

#     return path, path_weights




# # Example usage
# path, path_weights = find_shortest_path(G, result, "M1", "M3")
# print("Path:", path)
# print("Path Weights:", path_weights)


# def decode_message(path_weights):
#     return ''.join(chr(64 + weight) for weight in path_weights)

# # Example usage
# message = decode_message(path_weights)
# print("Secret Message:", message)
