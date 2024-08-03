# 校验码数组
jiaoyan = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2]
high = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]


def cal_sum(s):
    tem = 0  # 初始化 tem
    for i in range(len(s) - 1):
        tem += high[i] * int(s[i])
    x = jiaoyan[tem % 11]
    if s[17] == str(x):
        return 0
    else:
        return 1

def birth(s):
    return [int(s[6:10]), int(s[10:12]), int(s[12:14])]

def cal_birth(list0, list_Birth):
    if (list0[0] - list_Birth[0]) < 18 or \
            ((list0[0] - list_Birth[0]) == 18 and (list0[1] < list_Birth[1])) or \
            ((list0[0] - list_Birth[0]) == 18 and (list0[1] == list_Birth[1]) and (list0[2] < list_Birth[2])):
        return 0
    else:
        return 1


# 输入处理
n = int(input())
birthCnt = 0
errorCnt = 0
list0 = list(map(int, input().split()))

# print(list0)

for i in range(n):
    s = str(input())
    # print(s)

    list_Birth = birth(s)
    birthCnt += cal_birth(list0, list_Birth)
    errorCnt += cal_sum(s)
print(birthCnt, errorCnt)
