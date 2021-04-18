a,c = map(int, input().split())
b,d = map(int, input().split())

if a>c:
    tmp = a
    a = c
    c = tmp
if b>d:
    tmp = b
    b = d
    d = tmp

if a<b and c<d:
    if c<b:
        print("not cross")
    else:
        print("cross")
elif a>b and c<d:
    print("not cross")
elif a<b and c>d:
    print("not cross")
else:
    if d<a:
        print("not cross")
    else:
        print("cross")