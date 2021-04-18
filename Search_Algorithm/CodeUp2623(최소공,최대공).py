a,b = map(int, input().split())
arr1 = []
arr2 = []
result = []
mul = 1

for i in range(2,a+1):
    if a != 1:
        for j in range(0, int(a/i)):
            if a % i ==0:
                arr1.append(i)
                a /= i
            else:
                break
            if a == 1:
                break
    else: 
        break
#print(arr1)

for i in range(2,b+1):
    if b != 1:
        for j in range(0, int(b/i)):
            if b % i ==0:
                arr2.append(i)
                b /= i
            else:
                break
            if b == 1:
                break
    else: 
        break
#print(arr2)

for i in range(0,len(arr1)):
    for j in range(0, len(arr2)):
        if arr1[i]!=-1 and arr2[j]!=-1 and arr1[i]==arr2[j]:
            result.append(arr1[i])
            arr1[i] = -1
            arr2[j] = -2
#print(result)

for i in range(0, len(result)):
    mul *= result[i]
print(mul)

"""
난 왜 최소 공배수를 구했을까,,
for i in range(1,a+1):
    for j in range(1,b+1):
        x = a*j
        y = b*i
        if(x==y):
            tmp = x
            if(result > tmp):
                print(tmp)
                result = tmp
                print(result)
print(result)
"""