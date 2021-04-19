input = list(input())

#num = []
sum = 0
alpha = []
result = []
for item in input:
    if 49<=ord(item)<=57:
        #num.append(int(item))
        sum += int(item)
    else:
        alpha.append(item)
#result = sorted(alpha)
alpha.sort()
for item in alpha:
    print(item,end='')
#print(sum(num))    
print(sum)     