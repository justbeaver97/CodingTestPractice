input = int(input())

for i in range(1,input+1):
    if i%3==0:
        continue
    else:
        print(i, end=' ')
print()