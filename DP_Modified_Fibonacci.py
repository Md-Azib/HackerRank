t1, t2, n = map(int, input().split())
arr = [0 for i in range(21)]
arr[1] = t1
arr[2] = t2
for i in range(3, 21):
    arr[i] = arr[i - 2] + (arr[i - 1] * arr[i - 1])
print(arr[n])

