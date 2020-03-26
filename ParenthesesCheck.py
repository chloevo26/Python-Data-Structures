def isValid (s):
    stack = []
    openList = ['(', '[', '{']
    matchList = [('(',')'), ('[', ']'), ('{', '}')]
    for i in s:
        if i in openList:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if (top,i) not in matchList:
                return False

    return len(stack) == 0


print(isValid('{}[]'))

