input1 = int(input())
input_arr = input().split()

for i in range(0, len(input_arr)):
    tmp = len(input_arr)-i-1
    print(input_arr[tmp], end=' ')
print()