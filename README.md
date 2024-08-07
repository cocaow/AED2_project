Algoritmo de Johnson para Caminhos Mínimos em Grafos com Pesos

O algoritmo de Johnson é um método eficiente para encontrar os caminhos mínimos entre todos os pares de vértices em um grafo com pesos, incluindo pesos negativos. Ele funciona adicionando um nó fictício conectado a todos os outros nós com arestas de peso zero, e então aplicando o algoritmo de Bellman-Ford a partir desse nó fictício para calcular um potencial que repondera os pesos das arestas, tornando-os não negativos. Após essa reponderação, o algoritmo de Dijkstra é usado a partir de cada nó para encontrar os caminhos mínimos, garantindo eficiência mesmo em grafos densos. O resultado final é ajustado para refletir os pesos originais, fornecendo as distâncias mínimas corretas entre todos os pares de nós.

O algoritmo de Johnson é composto por dois algoritmos principais: o algoritmo de Bellman-Ford e o algoritmo de Dijkstra. Além disso, ele envolve um processo de reponderação das arestas. A seguir, explico cada um desses componentes:

### Algoritmo de Bellman-Ford

O algoritmo de Bellman-Ford é usado para encontrar os caminhos mínimos de um único vértice fonte para todos os outros vértices em um grafo, mesmo quando esse grafo contém arestas com pesos negativos. Ele funciona relaxando repetidamente todas as arestas do grafo, permitindo que as distâncias mínimas sejam ajustadas de forma incremental. O Bellman-Ford é especialmente útil porque pode detectar a presença de ciclos de peso negativo, o que é crucial para a correção do algoritmo de Johnson. Se for encontrado um ciclo de peso negativo, o algoritmo sinaliza que a solução não é possível.

### Algoritmo de Dijkstra

O algoritmo de Dijkstra é usado para encontrar os caminhos mínimos de um único vértice fonte para todos os outros vértices em um grafo com pesos não-negativos. Ele usa uma fila de prioridade para explorar os vértices de forma eficiente, sempre expandindo o vértice com a menor distância conhecida até que todas as menores distâncias tenham sido determinadas. O Dijkstra é rápido e eficiente para grafos sem pesos negativos, e é usado repetidamente no algoritmo de Johnson após a reponderação das arestas para calcular os caminhos mínimos ajustados.

### Reponderação das Arestas

A reponderação das arestas é uma técnica utilizada no algoritmo de Johnson para transformar o grafo original, possivelmente contendo arestas com pesos negativos, em um grafo equivalente onde todas as arestas têm pesos não-negativos. Isso é feito adicionando um vértice fictício ao grafo e usando o algoritmo de Bellman-Ford para calcular uma função de potencial (ou valor de reponderação) para cada vértice. As arestas do grafo são então ajustadas para que os pesos se tornem não-negativos, permitindo o uso do algoritmo de Dijkstra. A reponderação garante que as distâncias mínimas originais possam ser recuperadas corretamente após os cálculos com Dijkstra.

Esses três componentes, trabalhando em conjunto, permitem que o algoritmo de Johnson encontre os caminhos mínimos entre todos os pares de vértices em um grafo que pode conter pesos negativos, sem ser afetado por ciclos de peso negativo.
