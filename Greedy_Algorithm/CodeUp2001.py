pasta = []
juice = []
result = 4000
for i in range(0,3):
    tmp = int(input())
    pasta.append(tmp)
for i in range(0,2):
    tmp = int(input())
    juice.append(tmp)

for i in range(0,3):
    for j in range(0,2):
        tmp = pasta[i]+juice[j]
        if result > tmp:
            result = tmp

print(format(result*1.1,".1f"))