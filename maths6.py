import math

def digit_sum(num):
    s = 0
    while num > 0:
        s += num % 10
        num = num // 10
    return s


n = int(input())
sqrt = n ** (0.5)
sqrt = math.floor(sqrt)
factors = []
for i in range(1, sqrt + 1):
    if n % i == 0:
        factors.append(i)
        if i != n // i:
            factors.append(n // i)
factors.sort()
#print(factors)
sm = []
for i in factors:
    sm.append(digit_sum(i))
#print(sm)
#print(max(sm))
index = 0
mx = 0
for i in range(len(sm)):
    if sm[i] > mx:
        mx = sm[i]
        index = i
print(factors[index])