input1, input2, input3, input4 = input().split()

a = int(input1)
m = int(input2)
d = int(input3)
n = int(input4)

for i in range(0,n-1):
    a*=m
    a+=d
print(a)