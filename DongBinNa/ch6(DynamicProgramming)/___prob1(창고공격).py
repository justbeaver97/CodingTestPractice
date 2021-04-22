n = int(input())
arr = list(map(int, input().split()))
print(arr)

sum=0
for i in range(n):
    for j in range(2+i,n):
        if arr[i]+arr[j]>sum:
            sum=arr[i]+arr[j]
            print('sum:',sum,'arr[i]:',arr[i],'arr[j]:',arr[j])
print(sum) 


d = [0]*10
d[0]=arr[0]
d[1]=max(arr[0],arr[1])
for i in range(2,n):
    d[i]=max(arr[i-1],arr[i-2]+arr[i])
print(d[n-2])