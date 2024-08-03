a = float(input())
cnt = 0
total = 0

while total <= a:
    total += 2 * (0.98 ** cnt)
    cnt += 1

print(cnt)