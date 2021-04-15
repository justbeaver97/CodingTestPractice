input = input()

tmp = ord('a')
num = ord(input)

while(tmp!=(num+1)):
    print(chr(tmp), end=' ')
    tmp+=1