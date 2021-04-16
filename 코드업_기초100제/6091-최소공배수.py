input1, input2, input3 = input().split()

num1 = int(input1)
num2 = int(input2)
num3 = int(input3)
tmp = []
final = []

for i in range(1,num1+1):
    for j in range(1, num2+1):
        tmp1 = i * num2
        tmp2 = j * num1
        if(tmp1==tmp2):
            tmp.append(tmp1)
#print(tmp)
num4 = tmp[0]

for i in range(1, num3+1):
    for j in range(1, num4+1):
        tmp3 = i * num4
        tmp4 = j * num3
        if tmp3==tmp4:
            final.append(tmp3)
print(final[0])