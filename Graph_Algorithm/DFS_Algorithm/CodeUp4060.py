def dfs(i,j):
    if i<0 or j<0 or i>=m or j>=n:
        return False
    if graph[i][j]==0:
        graph[i][j] = 2
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i-1,j)
        dfs(i,j-1)
        return True
    return False

def dfs2(i,j):
    if i<0 or j<0 or i>=m or j>=n:
        return False
    if graph[i][j]==1:
        graph[i][j] = 2
        dfs2(i+1,j)
        dfs2(i,j+1)
        dfs2(i-1,j)
        dfs2(i,j-1)
        return True
    return False

m,n = map(int, input().split())

graph=[]
for i in range(m):
    graph.append(list(map(int, input().split())))

result1, result2 = 0, 0 
for i in range(m):
    for j in range(n):
        if dfs(i,j) == True:
            result1 += 1
for i in range(m):
    for j in range(n):
        if dfs2(i, j) == True:
            result2 += 1
print(result1, result2)




""" 5 6
0 0 1 0 1 1
0 1 1 0 0 0
0 0 1 0 0 0
1 1 1 1 1 1
0 0 0 1 0 0 """

"""4 5
0 0 1 1 0
0 0 0 1 1
1 1 1 1 1
0 0 0 0 0"""