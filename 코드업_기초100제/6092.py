input1 = int(input())
input_arr = input().split()
final = []

for i in range(0,23):
    final.append(0)

for i in range(0,input1):
    tmp = int(input_arr[i])
    final[tmp-1]+=1

for i in range(0,23):
    print(final[i], end=' ')
print()