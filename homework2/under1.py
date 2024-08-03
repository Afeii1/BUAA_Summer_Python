def cal_sum(list0):
    a = list0[0]
    b = list0[1]
    for i in range(2, 20):  # Only calculate up to the 20th element
        c = a + b
        list0.append(c)
        a = b
        b = c


try:
    m = int(input())
    n = int(input())

    if -100 <= m <= 100 and -100 <= n <= 100:
        list0 = [m, n]
        cal_sum(list0)
        print(sum(list0))
    else:
        print("illegal input")
except ValueError:
    print("illegal input")
