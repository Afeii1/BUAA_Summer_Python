str1 = str(input())
str2 = str(input())
result = []

for i in range(len(str1)):
    for j in range(len(str2)):
        k = 0
        temp = []
        while (
            (i + k) < len(str1) and (j + k) < len(str2) and str1[i + k] == str2[j + k]
        ):
            temp.append(str1[i + k])
            k = k + 1
            if k > len(result):
                result = temp
if result:
    print(''.join(result))
else:
    print("No Answer")