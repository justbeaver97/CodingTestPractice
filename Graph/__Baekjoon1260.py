def dfs(v):
    visited[v] = True
    print(visited)
    print(v,end=' ')
    for i in range(1,n+ 1):
        if visited[i]==False and graph[x][i]==1:
            dfs(i)

def bfs(v):
    pass

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for i in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

print(graph)
dfs(v)
print()
bfs(v)

"""
4 5 1
1 2
1 3
1 4
2 4
3 4
"""