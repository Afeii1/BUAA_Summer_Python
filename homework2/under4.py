def josephus(n, k, index):
    # 初始化列表
    List = [i for i in range(1, n + 1)]

    # 调整index以适应0-based index
    index -= 1

    while len(List) > 1:
        # 计算下一个要删除的人的索引
        index = (index + k - 1) % len(List)
        # 移除该人
        List.pop(index)

    # 剩下的最后一个人就是答案
    return List[0]


if __name__ == '__main__':
    # 读取输入
    input_data = input().split()
    n = int(input_data[0])
    k = int(input_data[1])
    index = int(input_data[2])

    # 输出结果
    result = josephus(n, k, index)
    print(result)
