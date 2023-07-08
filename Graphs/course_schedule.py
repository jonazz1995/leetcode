
def courseSchedule(CourseNum, prereq):
    preMap = get_graph()
    visited = set()

    def dfs(crs):
        if preMap[crs] == []:
            return True
        
        if crs in visited:
            return False
        
        visited.add(crs)

        for neighbour in preMap[crs]:
            dfs(neighbour)



    def get_graph(lst):
        graph = {}

        for a, b in lst:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append(b)
        return graph

lst = [[0,1], [0,2], [1,3], [1,4], [3,4]]
print(get_graph(lst))

