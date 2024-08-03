n = int(input())
list0 = list(map(int, input().split()))
list1 = list(map(int, input().split()))

sum0 = 0
ans = 0

temp = 0

# for i in range(0, n):
#     for j in range(i, n):
#         temp += list0[i] * list1[j]
#
# print(temp)

for i in range(n - 2, -1, -1):
    sum0 += list1[i + 1]
    ans += list0[i + 1] * sum0

ans += (sum0 + list1[0]) * list0[0]
print(ans)


