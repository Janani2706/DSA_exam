def balanced_brackets(s):
    stack=[]
    brackets={')':'(', '}':'{', ']':'['}
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return False
    return not stack
s=input("Enter the String : ")
result=balanced_brackets(s)
if result:
    print("YES")
else:
    print("NO")