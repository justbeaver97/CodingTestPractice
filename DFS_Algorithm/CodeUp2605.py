def dfs(i,j,k):
    if i<0 or j<0 or i>=7 or j>=7:
        return False
    if graph[i][j]==k:
        stack.append([i,j])
        graph[i][j] = 0
        dfs(i+1,j,k)
        dfs(i,j-1,k)
        dfs(i-1,j,k)
        dfs(i,j+1,k)
        if len(stack)>=3:
            return True
    return False

graph=[]
for i in range(7):
    graph.append(list(map(int, input().split())))

result = 0
stack=[]
for k in range(1,6):
    for i in range(7):
        for j in range(7):
            if dfs(i,j,k)==True:
                result += 1
            stack=[]
print(result)