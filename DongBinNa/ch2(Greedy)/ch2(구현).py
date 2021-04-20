#1 Matrix 
for i in range(0,5):
    for j in range(0,5):
        print('(',i,',',j,')', end=' ')
    print()

#2 방향 벡터 - 동서남북
dx = [0,-1,0,1]
dy = [1,0,-1,0]
x, y = 2, 2
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    print("현재위치: (",nx,",",ny,")")

