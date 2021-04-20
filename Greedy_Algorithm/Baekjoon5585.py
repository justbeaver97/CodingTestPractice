input = int(input())

coins =[500,100,50,10,5,1]

money = 1000-input      #420
count = 0

for coin in coins:
    tmp = 0 
    tmp = money//coin   #4
    money -= tmp*coin
    count += tmp
print(count)