import math
for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        sqrt = n ** (0.5)
        sqrt = math.floor(sqrt)
        factors = []
        for i in range(1, sqrt + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
        count = 0
        for i in factors:
            if i % 2 == 0:
                count += 1
        print(count)
    else:
        print(0)

