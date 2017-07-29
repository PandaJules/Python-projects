def is_matched(expression):
    pairs = {'{' : '}', '[' : ']', '(' : ')'}
    stack = []
    for char in expression:
        if char in pairs:
            stack.append(pairs[char])
        elif stack and char == stack[-1]:
                stack.pop()
        else: 
            return False
    if stack==[]:
        return True
    else:
        return False