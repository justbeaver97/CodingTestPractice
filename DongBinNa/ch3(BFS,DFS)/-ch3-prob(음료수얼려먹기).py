# def dfs(x,y):
#     if x<=-1 or y<=-1 or x>=n or y>=m:
#         return False
#     if graph[x][y]==0:
#         graph[x][y]=1
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         return True
#     return False

# n, m = map(int, input().split())

# graph = []
# for i in range(0,n):
#     graph.append(list(map(int, input())))

# result = 0
# for i in range(0,n):
#     for j in range(0,m):
#         if dfs(i,j) == True:
#             result += 1
# print(result)



# 4 5
# 00110
# 00011
# 11111
# 00000


def dfs2(i,j):
    if i<0 or i>=n or j<0 or j>=m:
        return False
    if arr[i][j] == 0:
        arr[i][j] = 1
        dfs2(i+1,j)
        dfs2(i,j+1)
        dfs2(i-1,j)
        dfs2(i,j-1)
        return True
    return False

n,m = map(int, input().split())
arr = []
for i in range(0,n):
    arr.append(list(map(int,input())))
result = 0
for i in range(0,n):
    for j in range(0,m):
        if dfs2(i,j)==True:
            result += 1
print(result)