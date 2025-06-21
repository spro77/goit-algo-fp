import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.edges[u].append((v, weight))

    def dijkstra(self, start):
        heap = [(0, start)]
        distances = {start: 0}
        visited = set()

        while heap:
            current_dist, u = heapq.heappop(heap)

            if u in visited:
                continue

            visited.add(u)

            for v, weight in self.edges[u]:
                if v in visited:
                    continue

                new_dist = current_dist + weight

                if v not in distances or new_dist < distances[v]:
                    distances[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        return distances

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    start_vertex = 'A'
    shortest_paths = g.dijkstra(start_vertex)
    print(f"Shortest paths from {start_vertex}: {shortest_paths}")

