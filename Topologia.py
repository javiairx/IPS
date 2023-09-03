import networkx as nx

# Creamos un objeto de grafo vacío
G = nx.Graph()

# Agregamos algunos nodos al grafo
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Agregamos algunas aristas al grafo
G.add_edge(1, 2)
G.add_edge(2, 3)

# Imprimimos algunas propiedades del grafo
print("Número de nodos:", G.number_of_nodes())
print("Número de aristas:", G.number_of_edges())
print("Lista de nodos:", list(G.nodes()))
print("Lista de aristas:", list(G.edges()))

# Visualizamos el grafo
nx.draw(G, with_labels=True)
