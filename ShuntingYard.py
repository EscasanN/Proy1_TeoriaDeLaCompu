def ShuntingYard(infix):
    operators = ["|", "*"]    
    stack = []
    postfix = ""
    temp = ""

    for c in infix:

        if c in operators:
            while True:
                if len(stack) != 0:
                    temp = stack.pop()
                    stack.append(temp)
                else:
                    temp = ""

                if c == "*" and temp == "|":
                    postfix += stack.pop()
                else:
                    break
            stack.append(c)
        elif c == "(":
            stack.append(c)
        elif c == ")":
            while stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
        else:
            postfix += c

    while len(stack) != 0:
        postfix += stack.pop()

    return postfix