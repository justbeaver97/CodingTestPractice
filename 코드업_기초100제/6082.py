input = int(input())

for i in range(1,input+1):
    if i<10:
        if i%3==0:
            print("X", end=' ')
        else:
            print(i, end=' ')
    else:
        if (i%10)%3==0 and i%10!=0:
            print("X", end=' ')
        else:
            print(i, end=' ')
print()