def area(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    x1 = max(Ax1, Bx1)
    y1 = min(Ay1, By1)
    x2 = min(Ax2, Bx2)
    y2 = max(Ay2, By2)

    width = x2 - x1
    height = y1 - y2

    if width <= 0 or height <= 0:
        return 0
    return width * height


Ax1, Ay1, Ax2, Ay2 = map(int, input().split())
Bx1, By1, Bx2, By2 = map(int, input().split())

print(area(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2))
