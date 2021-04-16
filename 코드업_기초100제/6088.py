input1, input2, input3 = input().split()

a = int(input1)
d = int(input2)
n = int(input3)

for i in range(0,n-1):
    a+=d
print(a)