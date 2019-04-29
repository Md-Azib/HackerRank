def count(n, arr, m):
    combinations = [0 for i in range(n + 1)]
    combinations[0] = 1
    for i in range(m):
        for j in range(arr[i], n + 1):
            combinations[j] += combinations[j - arr[i]]
    return combinations[n]


n, m = map(int, input().split())
arr = list(map(int, input().split()))
c = count(n, arr, m)
print(c)




