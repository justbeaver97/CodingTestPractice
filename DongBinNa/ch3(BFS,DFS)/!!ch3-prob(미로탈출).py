''' def dfs(i,j):
    if i<0 or j<0 or i>=n or j>=m:
        return False
    if graph[i][j] == 1:
        stack.append([i,j])
        graph[i][j] = 0
        x, y, z, w = dfs(i+1,j), dfs(i,j+1), dfs(i-1,j), dfs(i,j-1)
        if x == False or y == False or z == False or w == False:
            stack.pop()
            a, b = stack[len(stack)-1][0], stack[len(stack)-1][1]
            graph[a][b] = 1
            dfs(a,b)
            return False
        return True
    return False '''

# stack = []
# dfs(0,0)
# print(len(stack))

def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                # print('x:',x,'y:',y,end=' ')
                # print('graph[nx][ny]:',graph[nx][ny], end=' ')
                # print('graph[x][y]:',graph[x][y])
                stack.append([x,y])
                queue.append((nx,ny))
    return graph[n-1][m-1]
            


from collections import deque

n, m = map(int, input().split())
stack = []
graph = []
for i in range(0,n):
    graph.append(list(map(int,input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(bfs(0,0))
print(stack)
print(graph)

""" 5 6
101010
111111
000001
111111
111111 """