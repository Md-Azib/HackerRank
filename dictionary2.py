for _ in range(int(input())):
    s1 = input()
    s2 = input()
    hash = {}
    flag = False
    for i in s1:
        hash[i] = 1
    for i in s2:
        try:
            if hash[i] == 1:
                flag = True
                break
        except KeyError:
            flag = False
    if flag:
        print('YES')
    else:
        print('NO')
