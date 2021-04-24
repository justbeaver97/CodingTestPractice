def dfs(i,j):
    if i<0 or j<0 or i>m-1 or j>n-1:
        return False
    if graph[i][j] == 0:
        graph[i][j]=1
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i+1,j)
        dfs(i,j-1)
        tmp.append([i,j])
        return True
    return False

m, n, k = map(int, input().split())
arr = []
for i in range(k):
    arr.append(list(map(int, input().split())))
graph = [[0]*n for i in range(m)]

for item in arr:                                
    for i in range(item[1],item[3]):            
        for j in range(item[0],item[2]):        
            graph[i][j]+=1

tmp = []
result = []
for i in range(m):
    for j in range(n):
        tmp = []
        dfs(i,j)
        if tmp!=[]:
            result.append(len(tmp))
tmp = sorted(result)
print(len(tmp))
for item in tmp:
    print(item, end=' ')
print()
"""
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
"""