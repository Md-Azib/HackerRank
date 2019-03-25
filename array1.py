for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = True
    count = 0
    for i in range(n - 1, -1, -1):
        #print(arr[i] - (i + 1))
        if arr[i] - (i + 1) > 2:
            flag = False
            break
        for j in range(max(0, (arr[i] - 2)), i):
            if arr[j] > arr[i]:
                count += 1
    if flag:
        print(count)
    else:
        print('Too chaotic')
