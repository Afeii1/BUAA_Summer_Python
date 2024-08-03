
n = int(input())

windows = []

for i in range(n):
    window_info = list(map(int, input().split()))
    windows.append(window_info)

nn = int(input())

for i in range(nn):
    x, y = map(int, input().split())

    clicked_window = -1
    for j in range(n):
        if windows[j][1] <= x <= windows[j][3] and windows[j][2] <= y <= windows[j][4]:
            clicked_window = j
            break

    if clicked_window != -1:
        clicked = windows.pop(clicked_window)
        windows.insert(0, clicked)

for window_info in windows:
    print(window_info[0], end=' ')
