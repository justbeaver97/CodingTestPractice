n, k = map(int, input().split())
n_arr = list(map(int, input().split()))
result = -1

for i in range(0,n):
    if k <= n_arr[i]:
        result = i+1
        break

if result == -1:
    print(n+1)
else:
    print(result)
