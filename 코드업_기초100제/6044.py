input1, input2 = input().split()

a = int(input1)
b = int(input2)

add = a + b
sub = a - b
mul = a * b
div = a // b
rest = a % b
num = format(a/b, ".2f")

print("{}\n{}\n{}\n{}\n{}\n{}".format(add, sub, mul, div, rest, num))