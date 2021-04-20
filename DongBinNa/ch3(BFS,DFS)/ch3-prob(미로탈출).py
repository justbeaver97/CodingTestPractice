def dfs(i, j):
    if i<0 or i>=n or j<0 or j>=n:
        return False
    if graph[i][j] == 1:
        graph[i][j] = 0
        if (dfs(i+1,j) == False and dfs(i,j+1) == False and dfs(i-1,j) == False and dfs(i,j-1) == False):
            if stack != []:
                stack.pop()
                if stack != []:
                    graph[stack[len(stack)-1][0],stack[len(stack)-1][1]]
                    dfs(stack[len(stack)-1][0],stack[len(stack)-1][1])
        stack.append([i,j])
        print(stack)
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i-1,j)
        dfs(i,j-1)
    return False

n,m = map(int, input().split())

graph = []
for i in range(0,n):
    graph.append(list(map(int, input())))

stack = []
i, j = 0, 0

dfs(i, j)
print(stack)


""" 5 6
101010
111111
000001
111111
111111 """