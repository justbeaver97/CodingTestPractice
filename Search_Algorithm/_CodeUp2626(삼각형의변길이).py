n = int(input())
arr1 = []
arr2 = []
tmp = []
tmp2 = []
result = []

if n < 3:
    print('0')
else:
    for i in range(1, n-1):
        for j in range(1, n-i):
            x=i
            y=j
            z=n-i-j
            arr1.append(sorted([x,y,z]))
    #print(arr1)

    for i in range(0,len(arr1)):
        if arr1[i][0]+arr1[i][1] > arr1[i][2]:
            arr2.append(arr1[i])
    tmp = sorted(arr2)
    #print(tmp)

    if tmp == []:
        print('0')
    else:
        j=0
        tmp2.append(tmp[j])
        result.append(tmp[j])
        for i in range(0,len(tmp)-1):
            if tmp2[j]!=tmp[i+1]:
                result.append(tmp[i+1])
                tmp2.append(tmp[i+1])
                j += 1
        #print(result)
        print(len(result))
