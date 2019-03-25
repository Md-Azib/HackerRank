n, r = map(int, input().split())
arr = list(map(int, input().split()))
r = r % n
arr = arr[r:] + arr[:r]
for i in arr:
    print(i, end=' ')
