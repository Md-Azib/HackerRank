n = int(input())
arr = list(map(int, input().split()))
start = 0
end = n - 1
length = n
prod1 = min(arr) * length
while start < end:
    if prod1 > min(arr[start:end + 1]) * length:
        print(prod1)
        break
    else:
        prod1 = min(arr[start:end + 1]) * length
    if arr[start] >= arr[end]:
        end -= 1
    elif arr[start] < arr[end]:
        start += 1
    length -= 1

