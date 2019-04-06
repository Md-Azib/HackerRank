for _ in range(int(input())):
    s = input()
    l = list(s)
    flag = False
    pivot = -1
    swap_index = -1
    length = len(l)
    for i in range(length - 1, 0, -1):
        if l[i] > l[i - 1]:
            pivot = i - 1
            flag = True
            break
    if not flag:
        print('no answer')
    else:
        for i in range(length - 1, pivot, -1):
            if l[i] > l[pivot]:
                swap_index = i
                break
        l[pivot], l[swap_index] = l[swap_index], l[pivot]
        temp = l[pivot + 1:]
        l = l[:pivot + 1]
        temp.sort()
        l = l + temp
        ans = ''
        ans = ans.join(l)
        print(ans)
