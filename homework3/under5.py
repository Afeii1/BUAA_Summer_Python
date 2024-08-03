def transform_expression(expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    result = []

    for token in expr:
        if token.isdigit():  # 如果是数
            result.append(token)
        elif token == '(':  # 左括号直接入栈
            stack.append(token)
        elif token == ')':  # 右括号则弹出直到左括号
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # 弹出左括号
        else:  # 操作符处理
            while stack and stack[-1] != '(' and precedence.get(token, 0) <= precedence.get(stack[-1], 0):
                result.append(stack.pop())
            stack.append(token)

    while stack:  # 弹出剩余的操作符
        result.append(stack.pop())

    return ''.join(result)


expr = str(input())
print(transform_expression(expr))
