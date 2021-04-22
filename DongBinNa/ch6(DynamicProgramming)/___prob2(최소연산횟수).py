''' n = int(input())
count = 0

while True:
    if n == 1:
        count += 1
        break
    if n<5:
        if n==2:
            n /= 2
            count += 1
        elif n==3:
            n /= 3
            count += 1
        elif n==4:
            n /= 2
            n /= 2
            count += 2
        if n == 1:
            break

    tmp = n%5
    n -= tmp
    count += tmp

    if n%2==0:
        n /= 2
        count += 1
    elif n%3==0:
        n /= 3
        count += 1
    elif n%5==0:
        n /=5
        count += 1
    else:
        n -= 1
        count += 1
print(count)  '''
#윗 부분은 틀렸을 가능성이 있음

#n = int(input())
n2 = int(input())
d = [0]*(n2+1)

for i in range(2,n2+1):
    d[i] = d[i-1]+1
    if i%2 == 0:
        d[i] = min(d[i],d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    if i%5 == 0:
        d[i] = min(d[i],d[i//5]+1)
print(d)
print(d[n2])