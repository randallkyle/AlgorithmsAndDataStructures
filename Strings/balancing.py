def isBalanced(s):
    ''' this takes a string of parentheses and makes sure that they are balanced '''
    stack = Stack()
    for i in s:
        if i in "{[(":
            stack.push(i)
        if i in "}])":
            j = stack.pop()
            if j == "{" and i != "}":
                return False
            if j == "[" and i != "]":
                return False
            if j == "(" and i != ")":
                return False
    return (stack.isEmtpy())
