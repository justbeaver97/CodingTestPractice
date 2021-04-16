input_num = int(input())
input_arr = input().split()

tmp = int(input_arr[0])
for i in range(0,input_num-1):
    if tmp > int(input_arr[i+1]):
        tmp = int(input_arr[i+1])
    else:
        tmp = tmp
print(tmp)