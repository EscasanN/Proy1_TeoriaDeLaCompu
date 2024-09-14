def ShuntingYard(infix):
    operators = ["|", "*"]    
    stack = []
    postfix = ""
    temp = ""

    for c in infix:
#        print(c)

        if c in operators:
            while True:
                if len(stack) != 0:
                    temp = stack.pop()
                    stack.append(temp)
                else:
                    temp = ""

                if temp == "*" and c == "|":
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

#        print(postfix)

    while len(stack) != 0:
        postfix += stack.pop()

    return postfix