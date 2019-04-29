#Balanced Brackets
for _ in range(int(input())):
    string = input()
    n = len(string)
    stack = []
    flag = 0
    for i in range(n):
        if string[i] == '(' or string[i] == '[' or string[i] == '{':
            stack.append(string[i])
        elif (string[i] == ')' or string[i] == '}' or string[i] == ']') and len(stack) > 0:
            if string[i] == ')':
                if stack[-1] == '(':
                    stack.pop(-1)
                else:
                    flag = 1
                    break
            if string[i] == '}':
                if stack[-1] == '{':
                    stack.pop(-1)
                else:
                    flag = 1
                    break
            if string[i] == ']':
                if stack[-1] == '[':
                    stack.pop(-1)
                else:
                    flag = 1
                    break
        else:
            flag = 1
            break
        #print(stack)
    if len(stack) != 0 or flag == 1:
        print('NO')
    else:
        print('YES')
