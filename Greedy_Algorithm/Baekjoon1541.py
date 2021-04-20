arr = list(input())
tmparr1 = []
tmparr2 = []

if arr.count('-') > 0:
    num = arr.index('-')
    tmparr1 = arr[:num+1]
    tmparr2 = arr[num:]
else:
    tmparr1 = arr

resultarr1 = []
resultarr2 = []
result1, result2, tmp, count = 0, 0, 0, 0

for i in range(0,len(tmparr1)):
    if tmparr1[i] == '+' or tmparr1[i] == '-':
        resultarr1.append(tmp)
        tmp = 0
    else:
        tmp1 = int(tmparr1[i])
        tmp = 10*tmp + tmp1
    if i == len(tmparr1)-1:
        resultarr1.append(tmp)
a = sum(resultarr1)

if tmparr2 != []:
    for i in range(0,len(tmparr2)):
        if tmparr2[i] == '+' or tmparr2[i] == '-':
            resultarr2.append(tmp)
            tmp = 0
        else:
            tmp1 = int(tmparr2[i])
            tmp = 10*tmp + tmp1
        if i == len(tmparr2)-1:
            resultarr2.append(tmp)
b = sum(resultarr2)
print(a-b)