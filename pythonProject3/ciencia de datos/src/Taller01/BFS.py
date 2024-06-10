from collections import deque

def bfs(graph, start):
    visited = set()  # Conjunto para mantener un registro de los nodos visitados
    queue = deque([start])  # Usamos una cola para los nodos por visitar

    while queue:
        vertex = queue.popleft()  # Tomamos el primer nodo de la cola
        if vertex not in visited:
            print(vertex)  # Visitamos el nodo (aquí simplemente lo imprimimos)
            visited.add(vertex)  # Marcamos el nodo como visitado
            # Agregamos los vecinos no visitados a la cola
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Grafo representado como un diccionario de listas de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Llamada al BFS comenzando desde el nodo 'A'
bfs(graph, 'A')
