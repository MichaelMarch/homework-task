import stack

while True:
    value = input()
    
    if value in ['+', '-', '*', '/']:
        left_operand = stack.pop()
        right_operand = stack.pop()
        stack.push(eval(f"{left_operand}{value}{right_operand}"))
        continue
    
    if value == '=':
        final_result = stack.pop()
        print(final_result)
        break
    
    stack.push(int(value))