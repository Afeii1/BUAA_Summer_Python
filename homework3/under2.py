list0 = list(map(str, input().split()))
num1 = int(list0[0])
num2 = int(list0[1])
op = ord(list0[2])
if op ==  ord('+'):
    print(num1 + num2)
elif op == ord('-'):
    print(num1 - num2)
elif op == ord('*'):
    print(num1 * num2)
elif op == ord('/'):
    if num2 != 0:
        if num1 % num2 == 0:
            print(num1 // num2)
        else:
            print(f'{num1 / num2: .2f}')
    else:
        print("Error: Division by zero")