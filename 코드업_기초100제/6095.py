num = int(input())
arr = []
board = [[0]*19 for y in range(19)]

for i in range(0,num):
    [row, col] = input().split()
    arr2 = [row, col]
    arr.append(arr2)
print(arr[1][0], arr[1][1])

for i in range(0,19):
    for j in range(0, 19):
        tmp1 = int(arr[i][0])
        tmp2 = int(arr[i][1])
        board[tmp1][tmp2] = 1

for i in range(0,19):
    for j in range(0,19):
        print(board[i],[j], end=' ')
    print()