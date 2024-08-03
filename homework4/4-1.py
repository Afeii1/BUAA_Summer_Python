n = int(input())
x = str(input())
y = str(input())
len1 = len(x)
len2 = len(y)
maxLength = max(len1, len2)
addition = 0

ans = []
x = x[::-1]
y = y[::-1]

for i in range(maxLength):
    num1 = int(x[i]) if i < len1 else 0
    num2 = int(y[i]) if i < len2 else 0
    result = num1 + num2 + addition
    addition = result // n
    ans.append(result % n)

if addition!= 0:
    ans.append(addition)

ans0 = ans[::-1]
print(''.join(map(str, ans0)))
