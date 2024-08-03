s = str(input())
print(s)
if len(s) == 3:
    num = int(s)
    a = num // 100
    b = (num // 10) % 10
    c = num % 10
    print(c*100 + b*10 + a)
else :
    print(-1)