s = input()
arr = []

for i in s:
    arr.append(int(i))

result = arr[0]
for i in range(0,len(arr)-1):
    if result<=1 and i<=1:
        result += arr[i+1]
    else:
        result *= arr[i+1]
print(result)