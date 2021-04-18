N, K = map(int, input().split())

coin = []
result = 0
for i in range(0,N):
    tmp = int(input())
    coin.append(tmp)

if K<5:
    for i in range(1,6):
        if K == i:
            result=i
else:
    for i in range(0,N):
        if K == 0:
            break
        if K > coin[N-1-i]:
            for j in range(0,6):
                if K == 0 :
                    break
                if K < j*coin[N-1-i]:
                    K -= (j-1)*coin[N-1-i]
                    result += (j-1)
                    break               
print(result)