from stack import Stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def isPatternBalanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "({[":
            s.Push(paren)
        else:
            if s.isEmpty():
                is_balanced = False
            else:
                top = s.Pop()
                if not is_match(top, paren):
                    is_balanced = False
    if s.isEmpty() and is_balanced:
        return True
    else:
        return False

print(isPatternBalanced("()"))
