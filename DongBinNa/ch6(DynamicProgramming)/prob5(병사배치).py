n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
print(arr)
# d=[]
# for i in range(n):
#     d.append(arr[i])
# result = 0
# for i in range(0,n-2):
#     if arr[i]<arr[i+1]:
#         if arr[i]>arr[i+2]:
#             d[i]=-1
#             print("i:",i,"d:",d)
#         elif arr[i]<arr[i+2]:
#             d[i]=-1
#             print("i:",i,"d:",d)
#     else:
#         print("i:",i,"d:",d)
# if d[n-2]!=-1:
#     if d[n-2]<d[n-1]:
#         d[n-1]=-1
# print(d)

d = [1]*(n+1)
for i in range(1,n):
    for j in range(0,i):
        if arr[j]<arr[i]:
            d[i]=max(d[i],d[j]+1)
print(n-max(d))

"""
7
15 11 4 8 5 2 4
7
15 4 8 5 11 4 2
"""