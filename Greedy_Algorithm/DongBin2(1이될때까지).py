N, K = map(int, input().split())
count = 0

''' while(True):
    if N==1:
        break
    elif N%K==0:
        N /= K
        count += 1
    else:
        N -= 1
        count += 1
print(count) '''

result = 0

while True:
    #N이 K로 나누어 떨어지는 수가 될때까지 빼주기
    target = (N // K) * K   #86 13 -> target = 78
    result += (N-target)    #result = 86-78 = 8
    N = target              #N = 78

    #더이상 나눌 수 없을때 반복문 탈출
    if N<K: break           #6<13 -> break

    #K로 나누기
    result += 1             #result 8 -> 9
    N //= K                 #78//13 -> N=6         

#마지막으로 남은 수에 대하여 1 빼기
result += (N-1)             #9 + (6-1) = 14 -> 마지막에 1이 남기 때문에 1을 빼줌
print(result)