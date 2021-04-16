input1, input2, input3, input4 = input().split()

h = int(input1)
b = int(input2)
c = int(input3)
s = int(input4)

result = ((h*b*c*s/8)/1024)/1024
print(format(result, ".1f"),"MB")