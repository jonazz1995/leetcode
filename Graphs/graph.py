# class GraphNode:
#     def __init__(self, data):
#         self.data = data
#         self.neighbours = []

#     def add_neighbour(self, neighbour):
#         self.neighbours.append(neighbour)


def dfs(graph, node, visited):
    if node in visited:
        return

    visited.add(node)

    print(node)

    for neighbour in graph[node]:
        dfs(graph, neighbour, visited)


from collections import deque
def bfs(graph, node):

    queue = deque([node])
    visited = set()

    while queue:
        curr = queue.popleft()
        if curr in visited:
            continue
        visited.add(curr)
        print(curr)

        for neighbour in graph[curr]:
            queue.append(neighbour)

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [7],
    5: [],
    6: [],
    7: []
}


print(dfs(graph, 1, set()))
print(bfs(graph, 1))