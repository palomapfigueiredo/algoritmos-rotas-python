import heapq

def dijkstra(graph, start):
    # Dicionário que armazena a menor distância de cada vértice até o vértice de origem
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Fila de prioridade para explorar os vértices mais próximos
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Verifica se a distância já processada é maior que a registrada
        if current_distance > distances[current_vertex]:
            continue

        # Explora os vizinhos do vértice atual
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Só atualiza a distância se for menor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Exemplo de uso
graph = {
    'Limeira': (0, 0),
    'Campinas': (30, 40),
    'Piracicaba': (50, 25),
    'Americana': (20, 35),
    'Hortolândia': (28, 42),
    'Santa Bárbara dOeste': (40, 20),
    'Sumaré': (22, 38),
    'Paulínia': (35, 45),
    'Indaiatuba': (60, 50),
    'Valinhos': (25, 48),
    'Vinhedo': (20, 55),
    'Itatiba': (15, 60),
    'Jundiaí': (12, 70),
    'Nova Odessa': (18, 33),
    'Monte Mor': (35, 30),
    'Cosmópolis': (15, 25),
    'Artur Nogueira': (10, 20),
    'Engenheiro Coelho': (5, 15),
    'Mogi Guaçu': (50, 5),
    'Araras': (55, 10),
    'Rio Claro': (60, 15)
}

start_vertex = 'Limeira'
distances = dijkstra(graph, start_vertex)

# Imprime a menor distância de cada vértice até o vértice de origem
print(f"Distâncias a partir do vértice {start_vertex}: {distances}")


