n = int(input())
sum1 = 0
sum2 = 0
sum3 = 0
for i in range(n * 3):
    line = list(map(str, input().split()))
    num = float(line[0])
    subject = line[1]
    if subject == "Math":
        sum1 += num
    if subject == "Chinese":
        sum2 += num
    if subject == "English":
        sum3 += num

print(f"{sum2 / n: .2f}")
print(f"{sum1 / n: .2f}")
print(f"{sum3 / n: .2f}")

