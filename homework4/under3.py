def lengthOfLIS(nums):
    tails, res = [0] * len(nums), 0
    for num in nums:
        i, j = 0, res
        while i < j:
            m = (i + j) // 2
            if tails[m] <= num:
                i = m + 1  
            else:
                j = m
        tails[i] = num
        if j == res: res += 1
    return res


s = input()
print(lengthOfLIS(list(s)))