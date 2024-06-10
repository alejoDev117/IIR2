def dfs(graph, start):
    visited = set()  # Conjunto para mantener un registro de los nodos visitados
    stack = [start]  # Usamos una pila para los nodos por visitar

    while stack:
        vertex = stack.pop()  # Tomamos el último nodo agregado a la pila
        if vertex not in visited:
            print(vertex)  # Visitamos el nodo (aquí simplemente lo imprimimos)
            visited.add(vertex)  # Marcamos el nodo como visitado
            # Agregamos los vecinos no visitados a la pila
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Grafo representado como un diccionario de listas de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Llamada al DFS comenzando desde el nodo 'A'
dfs(graph, 'A')
