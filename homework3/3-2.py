list0 = ['0','1','2','3','4','5','6','7','8','9',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
         'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
input_str = str(input())
ans = []

i = 0
while i < len(input_str):
    if input_str[i] == '-' and 1 <= i <= len(input_str) - 2:
        left = input_str[i - 1]
        right = input_str[i + 1]
        if left in list0 and right in list0 and list0.index(left) < list0.index(right):
            num_left = list0.index(left)
            num_right = list0.index(right)
            for num in range(num_left + 1, num_right):
                ans.append(list0[num])
        else:
            ans.append(input_str[i])
    else:
        ans.append(input_str[i])
    i += 1

print(''.join(ans))
