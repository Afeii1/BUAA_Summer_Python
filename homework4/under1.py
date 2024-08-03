n = int(input())
list0 = []
list1 = []

for i in range(n):
    a, b = input().split()
    list0.append(a)
    list1.append(int(b))

mm = list(zip(list0, list1, range(n)))
mm_sorted = sorted(mm, key=lambda x: (-x[1], x[2]))

for i in mm_sorted:
    print(f"{i[0].rjust(15, ' ')}{str(i[1]).rjust(5, ' ')}")
