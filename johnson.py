import heapq

def johnson(graph):
    # Adiciona um novo vértice fictício 's' ao grafo
    s = 's'
    graph[s] = {v: 0 for v in graph}

    # Passo 1: Usa Bellman-Ford para encontrar as menores distâncias de s para cada vértice
    h = bellman_ford(graph, s)
    if h is None:
        raise ValueError("O grafo contém ciclos de peso negativo.")

    # Remove o vértice fictício 's' do grafo
    del graph[s]

    # Passo 2: Repondera as arestas do grafo original
    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = {}
        for v in graph[u]:
            reweighted_graph[u][v] = graph[u][v] + h[u] - h[v]

    # Passo 3: Usa Dijkstra para encontrar os caminhos mínimos de cada vértice
    all_pairs_shortest_paths = {}
    for u in reweighted_graph:
        all_pairs_shortest_paths[u] = dijkstra(reweighted_graph, u)

    # Passo 4: Ajusta as distâncias finais
    for u in all_pairs_shortest_paths:
        for v in all_pairs_shortest_paths[u]:
            all_pairs_shortest_paths[u][v] += h[v] - h[u]

    return all_pairs_shortest_paths

# Função de Bellman-Ford
def bellman_ford(graph, source):
    distance = {v: float('inf') for v in graph}
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]

    for u in graph:
        for v in graph[u]:
            if distance[u] + graph[u][v] < distance[v]:
                return None  # Detecta ciclo de peso negativo

    return distance

# Função de Dijkstra
def dijkstra(graph, source):
    distance = {v: float('inf') for v in graph}
    distance[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        dist_u, u = heapq.heappop(priority_queue)
        if dist_u > distance[u]:
            continue
        for v in graph[u]:
            alt = dist_u + graph[u][v]
            if alt < distance[v]:
                distance[v] = alt
                heapq.heappush(priority_queue, (alt, v))

    return distance