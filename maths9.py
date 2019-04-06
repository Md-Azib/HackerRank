import math
l, s1, s2 = map(int, input().split())
for _ in range(int(input())):
    q = int(input())
    a = math.cos(0.785398)
    rootq = math.sqrt(q)
    t = (l - rootq) / (abs(s2 - s1) * a)
    print(format(t, '0.20f'))
