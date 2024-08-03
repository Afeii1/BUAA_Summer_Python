def remove_comments(code):
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    return code

def process_code(code):
    max_nesting_level = 0
    current_level = 0
    brace_sequence = []

    for char in code:
        if char == '{':
            current_level += 1
            brace_sequence.append('{')
            if current_level > max_nesting_level:
                max_nesting_level = current_level
        elif char == '}':
            brace_sequence.append('}')
            current_level -= 1

    return max_nesting_level, ''.join(brace_sequence)

import re

# Read the content of input.c
with open('input.c', 'r') as file:
    code = file.read()

cleaned_code = remove_comments(code)

max_level, braces = process_code(cleaned_code)

print(max_level)
print(braces)
