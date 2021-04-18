n, k = map(int, input().split())
n_arr = list(map(int, input().split()))
sum = 0
result = 0

for i in range(0, len(n_arr)):
    for j in range(i, len(n_arr)):
        sum += n_arr[j]
        if sum == k:
            result += 1
            break
        elif sum > k:
            print(n_arr[j], sum)
            break
    sum = 0
print(result)


# 10 11
# 4 7 9 3 4 7 4 2 7 2 
# 4