n, m = map(int, input().split())

coins = []
for i in range(n):
    tmp=int(input())
    coins.append(tmp)

d = [m+1]*(m+1)
d[0]=0

for i in range(coins[0],m+1):
    for coin in coins:
        d[i]=min(d[i],d[i-coin]+1)
if d[m]==n*m:
    result = -1
else:
    result = d[m]
print(d)
print(result)