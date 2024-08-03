def cal(x):
    if 0 <= x < 60:
        return 0
    else:
        return 4 - 3 * pow(100 - x, 2) / 1600

n = int(input())
listScore = []
listKey = []
sumGpa = 0

for i in range(n):
    score, key = map(float, input().split())
    if key >= 1:
        listScore.append(score)
        listKey.append(key)

for index in range(len(listScore)):
    score = listScore[index]
    sumGpa += cal(score) * listKey[index]

averageGpa = sumGpa / sum(listKey)

print(f"{averageGpa:.2f}")
