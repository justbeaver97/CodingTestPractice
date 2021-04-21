def dfs(i,j,k):
    if i<0 or j<0 or i>=m or j>=n:
        return False
    if k == 0:
        if graph[i][j]==k:
            pass
    if k == 1:
        if graph[i][j]==k:
            pass




m,n = map(int, input().split())

graph=[]
for i in range(m):
    graph.append(list(map(int, input().split())))

result=0 
for i in range(m):
    for j in range(n):
        if dfs(i,j,1) == True:
            result += 1