n = int(input())
table = {}
for i in range(n):
    s = input()
    try:
        table[s] += 1
    except:
        table[s] = 1
count = []
m = int(input())
for i in range(m):
    sample = input()
    try:
        count.append(table[sample])
    except:
        count.append(0)
for i in count:
    print(i)
