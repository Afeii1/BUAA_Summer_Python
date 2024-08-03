def solveNQueens(n) :
    m = n * 2 - 1
    ans = []
    col = [0] * n
    on_path, diag1, diag2 = [False] * n, [False] * m, [False] * m

    def dfs(r) :
        if r == n:
            ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in col])
            return
        for c, on in enumerate(on_path):
            if not on and not diag1[r + c] and not diag2[r - c]:
                col[r] = c
                on_path[c] = diag1[r + c] = diag2[r - c] = True
                dfs(r + 1)
                on_path[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场

    dfs(0)
    return ans

x, y = map(int, input().split())
x  = x - 1
y  = y - 1
ans = solveNQueens(8)
cnt = 0
for i in ans:
    if i[x][y] == 'Q':
        cnt += 1

print(cnt)