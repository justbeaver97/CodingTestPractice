def dfs(v):
    visited[v]=True
    for num in arr[v]:
        if visited[num]==False:
            dfs(num)
            result.append(num)

n = int(input())
l = int(input())
arr = [[0] for _ in range(n+1)]

for i in range(l):
    tmp, tmp2 = map(int, input().split())
    arr[tmp].append(tmp2)
    arr[tmp2].append(tmp)
for item in arr:
    item.remove(0)

result = []
visited=[False]*(n+1)
dfs(1)
# print(result)
print(len(result))

"""
7
6
4 5
6 4
7 2
3 5
3 1
1 5

4
"""