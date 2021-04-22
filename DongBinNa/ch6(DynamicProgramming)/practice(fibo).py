def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)

print(fibo(5)) 

y = []
y.append(1)
y.append(1)
result = 0

for i in range(0,101):
    result = y[i-2] + y[i-1]
    y.append(result)

print(y[1],y[98],y[99],y[100])