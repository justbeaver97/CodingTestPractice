a, b = map(int, input().split())
tempUp = [1, 5, 10]
tempDown = [-1, -5, -10]
result = 0

if a<b:
    diff = b-a
    for i in range(0,3):
        for j in range(0,5):
            if diff == 0:
                break
            if diff < j*tempUp[i]:
                diff -= (j-1)*tempUp[i]
                result += j
            elif diff == j*tempUp[i]:
                diff -= j*tempUp[i]
                result += j
        if diff == 0:
            break
elif a>b:
    diff = b-a
    for i in range(0,3):
        for j in range(0,5):
            if diff == 0:
                break
            if diff >= j*tempDown[i]:
                diff -= j*tempDown[i]
                result += j
        if diff == 0:
            break
else:
    result = 0
print(result)