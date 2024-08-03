import re

# 读取文件内容
with open('in.c', 'r') as f:
    lines = f.readlines()

identifiers = []

# 使用正则表达式匹配标识符
pattern = '[a-zA-Z_][a-zA-Z0-9_]*'
str =''
for line in lines:
    # 使用正则表达式找到所有标识符
    found_identifiers = re.findall(pattern, line)
    identifiers.extend(found_identifiers)

# 输出所有找到的标识符
for identifier in identifiers:
    if identifier == "if" or identifier == "else" or identifier == "for" or identifier == "while" or identifier == "switch" or  identifier == "case" :
        str = str + identifier;

with open('out.txt', 'w') as f:
    if str:
        f.write(str)
    else:
        f.write("No answer")