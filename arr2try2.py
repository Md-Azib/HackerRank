n = int(input())
arr = list(map(int, input().split()))
table = {}
count = 0
for i in range(n):
    table[i + 1] = False
for i in range(n):
    if arr[i] != i + 1 and not table[arr[i]]:
        count += 1
        table[arr[i]] = True
        table[i + 1] = True
    table[arr[i]] = True
print(count)
