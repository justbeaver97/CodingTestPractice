n = int(input())
count = 0

for i in range(0,n+1):
    for j in range(60):
        for k in range(60):
            # if i%10==3 or j%10==3 or k%10==3 or i//10==3 or j//10==3 or k//10==3:
            #     count += 1
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)
