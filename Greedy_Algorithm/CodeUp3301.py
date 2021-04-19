n = int(input())
money = [10,50,100,500,1000,5000,10000,50000]
count = 0

for i in range(0,len(money)):
    j=1
    while(True):
        if n < j*money[len(money)-1-i]:
            n -= (j-1)*money[len(money)-1-i]
            count += (j-1)
            #print(n, count)
            break
        j += 1
print(count)