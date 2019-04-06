factorial = []
factorial.append(1)
factorial.append(1)
for i in range(2, 2001):
    factorial.append(i * factorial[i - 1])


for _ in range(int(input())):
    zero, one = map(int, input().split())
    one -= 1
    a = (factorial[zero + one] // (factorial[one] * factorial[zero])) % 1000000007
    print(a)
