for _ in range(int(input())):
    n, k = map(int, input().split())
    s = []
    for i in range(n):
        s.append(i)
    mid = n // 2
    i = 0
    final = []
    while i != mid:
        final.append(s[n - 1 - i])
        final.append(s[i])
        i += 1
    final.append(s[mid])
    #print(final)
    print(final.index(k))

