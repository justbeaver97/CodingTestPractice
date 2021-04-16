input1, input2, input3 = input().split()

w = int(input1)
h = int(input2)
b = int(input3)

result = ((w*h*b/8)/1024)/1024
print(format(result, ".2f"),"MB")