N = int(input())

tmp1 = int(N/3) + 1
tmp2 = int(N/5) + 1
tmp3 = 0
result = N

for i in range(0,tmp1):
    for j in range(0,tmp2):
        x = 3*i
        y = 5*j
        if(x+y==N):
            tmp3 = i+j
            if(result>=tmp3):
                result = tmp3
if(result==N):
    result = -1
print(result)