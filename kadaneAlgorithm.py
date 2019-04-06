arr = list(map(int, input().split()))
maxEnd = 0
mx = 0
for i in range(len(arr)):
    if maxEnd + arr[i] > 0:
        maxEnd += arr[i]
    if maxEnd > mx:
        mx = maxEnd
print(mx)
