# input = int(input())
# sum=0
# tmp=0
# i=1

# while(sum!=input):
#     sum += i
#     tmp=i
#     i += 1
# print(tmp)

input = int(input())
sum = 0

for i in range(1,1001):
    sum += i
    if sum == input:
        tmp = i
print(tmp)

#54-10 55-10 56-11