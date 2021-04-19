n = int(input())
data = list(input().split())
print(data)
move = [[0,-1],[0,1],[-1,0],[1,0]]
arr = []

current = [1,1]
count = 0
while True:
    if count == len(data): break
    if data[count]=='L':
        if (current[1]-1)==0:
            count += 1
            continue
        else:
            count += 1
            current[1] -= 1
    elif data[count]=='R':
        if (current[1]+1)==(n+1):
            count += 1
            continue
        else:
            count += 1
            current[1] += 1
    elif data[count]=='U':
        if (current[0]-1)==0:
            count += 1
            continue
        else:
            count += 1
            current[0] -= 1
    elif data[count]=='D':
        if (current[0]+1)==(n+1):
            count += 1
            continue
        else:
            count += 1
            current[0] += 1
    else: pass
    print(current, end='   ')
print()
print(current)