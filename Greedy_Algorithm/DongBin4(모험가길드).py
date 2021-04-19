#굳이 모든 사람이 갈 필요가 없음 -> 공포도가 가장 낮은 사람들끼리만 가면 됨
''' n = int(input())
arr = list(map(int, input().split()))
count = 0
result = []

while True:
    if arr == []:
        break
    tmp = max(arr)
    tmp_arr = []
    for i in range(0,tmp):
        tmp_arr.append(max(arr))
        arr.remove(max(arr))
    result.append(tmp_arr)
print(len(result))
'''

n = int(input())
arr = list(map(int, input().split()))
count = 0
result = 0

for i in arr:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)