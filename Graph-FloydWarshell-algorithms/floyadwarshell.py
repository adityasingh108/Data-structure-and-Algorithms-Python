# The floyd-warshell algorithm Solve the problem of all pair shortest path in graph  using adject matrix


inf = 99999

def print_solution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if (distance[i][j] == inf):
                print('inf', end=' ')
            else:
                print(distance[i][j], end=' ')
        print(' ')

def floydWarshell(nV, graph):
    distance = graph
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])
    print_solution(nV, distance)
graph = [[0, 8, inf, 1],
         [inf, 0, 1, inf],
         [4, inf, 0, inf],
         [inf, 2, 9, 1],
         ]

floydWarshell(4,graph)



