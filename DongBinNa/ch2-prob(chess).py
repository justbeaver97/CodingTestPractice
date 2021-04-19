input = input()
count = 0
num = 97
arr = dict()
for i in range(1,9):
    for j in range(1,9):
        tmp = chr(num+(i-1))+str(j)
        arr[tmp]=[i,j]

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

for key,values in arr.items():
    if input == key:
        x, y = values[0], values[1]

for i in range(0,8):
    x1 = x + dx[i]
    y1 = y + dy[i]
    if 0<x1<9 and 0<y1<9:
        count += 1
print(count)