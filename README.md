Algoritmo de Johnson para Caminhos Mínimos em Grafos com Pesos

O algoritmo de Johnson é um método eficiente para encontrar os caminhos mínimos entre todos os pares de vértices em um grafo com pesos, incluindo pesos negativos. Ele funciona adicionando um nó fictício conectado a todos os outros nós com arestas de peso zero, e então aplicando o algoritmo de Bellman-Ford a partir desse nó fictício para calcular um potencial que repondera os pesos das arestas, tornando-os não negativos. Após essa reponderação, o algoritmo de Dijkstra é usado a partir de cada nó para encontrar os caminhos mínimos, garantindo eficiência mesmo em grafos densos. O resultado final é ajustado para refletir os pesos originais, fornecendo as distâncias mínimas corretas entre todos os pares de nós.

