import math
for _ in range(int(input())):
    l, b = map(int, input().split())
    area = l * b
    sqrt = math.floor(math.sqrt(area))
    #print(sqrt)
    #print(area)
    mx = 0
    for i in range(1, sqrt + 1):
        if area % (i * i) == 0 and l % i == 0 and b % i == 0 and (i * i) > mx:
            mx = i * i

    print(area // mx)
