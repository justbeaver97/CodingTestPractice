#1 stack
stack = []      #stack은 별다른 선언 없이 그냥 list로 선언하면 됨

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1], stack)

#2 queue
from collections import deque
queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() #deque는 양쪽 출입이 가능
queue.append(1)
queue.append(4)
queue.popleft()

print(queue, end=' ')
queue.reverse()
print(queue)


#3 recursive function -> stack 과 비슷한 논리
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

def gcd(a,b):
    # tmp = a%b
    # if tmp == 0:
    #     return b
    # a = b
    # b = tmp
    # return gcd(a,b)
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
print(gcd(192,162))