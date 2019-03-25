
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
q = int(input())
for i in range(q):
    count = 0
    n = int(input())
    if n == 1:
        print(0)
    else:
        prod = 1
        for j in range(len(prime)):
            prod *= prime[j]
            if prod <= n:
                count += 1
            else:
                break
        print(count)
hfds