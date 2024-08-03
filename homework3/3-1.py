list0 = list(map(str,input().split()))
ans = []
for i in range(len(list0)):
    if ans.count(list0[i]) == 0:
        ans.append(list0[i])
    else:
        pass

ans.sort()
for i in ans:
    print(i, end=' ')