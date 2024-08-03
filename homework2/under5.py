def is_divisible_by_all(num, divisors):
    return all(num % d == 0 for d in divisors)

def generate_palindromes():
    # 生成所有10到10^8之间的回文数
    palindromes = []
    # 处理长度为2到8的回文数
    for length in range(2, 9):
        if length % 2 == 0:  # 偶数长度
            half_length = length // 2
            start = 10 ** (half_length - 1)
            end = 10 ** half_length
            for i in range(start, end):
                s = str(i)
                palindromes.append(int(s + s[::-1]))
        else:  # 奇数长度
            half_length = length // 2
            start = 10 ** half_length
            end = 10 ** (half_length + 1)
            for i in range(start, end):
                s = str(i)
                palindromes.append(int(s + s[-2::-1]))
    return palindromes


if __name__ == "__main__":
    n = int(input())
    divisors = []
    for i in range(n):
        divisors.append(int(input()))

    palindromes = generate_palindromes()

    found_palindromes = []
    for p in palindromes:
        if is_divisible_by_all(p, divisors):
            found_palindromes.append(p)

    if found_palindromes:
        for p in found_palindromes:
            print(p)
    else:
        print("None")
