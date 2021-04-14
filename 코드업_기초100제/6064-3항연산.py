input1, input2, input3 = input().split()

a = int(input1)
b = int(input2)
c = int(input3)

print((a if a<b else b) if ((a if a<b else b)<c) else c)