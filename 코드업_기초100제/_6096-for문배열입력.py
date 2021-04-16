arr = []

for i in range(0,19):
    input_arr = input().split()
    arr.append(input_arr)

input1 = int(input())
num = []
for i in range(0,input1):
    row, col = map(int, input().split())
    row_col = [row, col]
    num.append(row_col)

for i in range(0,input1):
    for j in range(0,19):
        if arr[num[i][0]-1][j] == 0:
            arr[num[i][0]-1][j] = 1
        else:
            arr[num[i][0]-1][j] = 0
    for j in range(0,19):
        if arr[j][num[i][0]-1] == 0:
            arr[j][num[i][0]-1] = 1
        else:
            arr[j][num[i][0]-1] = 0

for i in range(0,19):
    for j in range(0,19):
        print(arr[i][j], end=' ')
    print()


