def caesar_encrypt(text, key):
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + key) % 26 + ord('A')))
        elif 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + key) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)

# 从标准输入读取加密密钥
key = int(input("Enter the encryption key (1-25): "))
if 1 <= key <= 25:
    # 读取文件 "in.txt" 的内容
    with open('in.txt', 'r') as infile:
        content = infile.read()
    # 加密内容
    encrypted_content = caesar_encrypt(content, key)
    # 将加密内容写入文件 "out.txt"
    with open('out.txt', 'w') as outfile:
        outfile.write(encrypted_content)

