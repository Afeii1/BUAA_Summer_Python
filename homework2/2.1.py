input_str = str(input())
ans = []

i = 0
while i < len(input_str):
    if input_str[i] == '-' and 1 <= i <= len(input_str) - 2:
        left = input_str[i - 1]
        right = input_str[i + 1]
        if left.isdigit() and right.isdigit() and left < right:
            num_left = int(left)
            num_right = int(right)
            for num in range(num_left + 1, num_right+1):
                ans.append(str(num))
            i += 1  # Skip the right character
        elif 'a' <= left <= 'z' and 'a' <= right <= 'z' and left < right:
            for char in range(ord(left) + 1, ord(right) + 1):
                ans.append(chr(char))
            i += 1  # Skip the right character
        elif 'A' <= left <= 'Z' and 'A' <= right <= 'Z' and left < right:
            for char in range(ord(left) + 1, ord(right) + 1):
                ans.append(chr(char))
            i += 1  # Skip the right character
        else:
            ans.append(input_str[i])
    else:
        ans.append(input_str[i])
    i += 1

print(''.join(ans))
