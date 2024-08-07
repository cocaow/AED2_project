import johnson

# Definição do grafo
graph = {
    'A': {'B': 1},
    'B': {'C': 3, 'E': 2},
    'C': {'A': 4},
    'D': {'C': 3, 'E': 1},
    'E': {'D': 1}
}

# Aplicar o algoritmo de Johnson
try:
    shortest_paths = johnson.johnson(graph)
    for start in shortest_paths:
        for end in shortest_paths[start]:
            print(f"Shortest path from {start} to {end}: {shortest_paths[start][end]}")
except ValueError as e:
    print(e)
