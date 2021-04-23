t = int(input())
result = [0]*t

for l in range(0,t):
    n, m = map(int, input().split())

    tmp = list(map(int, input().split()))
    matrix = []
    for i in range(0,n):
        matrix.append(tmp[i*m:(i+1)*m])
    d = [[0]*m for i in range(0,n)]

    for i in range(0,n):
        d[i][0] = matrix[i][0]
    for i in range(1,m):
        for j in range(0,n):
            if j==0:
                d[j][i] = max(d[j+1][i-1],d[j][i-1])+matrix[j][i]
            elif j==n-1:
                d[j][i] = max(d[j][i-1],d[j-1][i-1])+matrix[j][i]
            else:
                d[j][i] = max(d[j+1][i-1],d[j][i-1],d[j-1][i-1])+matrix[j][i]
        #print(d)
    for i in range(0,n):
        result[l]=max(result[l],d[i][m-1])
for item in result:
    print(item)



"""
2
3 4 
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2


1
3 4 
1 3 3 2 2 1 4 1 0 6 4 7
"""