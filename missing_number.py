def binarysearch(num):
    i = 0
    j = len(brr) - 1
    while i <= j:
        mid = (i + j) // 2
        if brr[mid] == num:
            return True
        elif brr[mid] > num:
            j = mid - 1
        elif brr[mid] < num:
            i = mid + 1
    return False


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
brr = list(map(int, input().split()))
seta = set(arr)
setb = set(brr)
setc = set()
setc = setb - seta
for i in setc:
    print(i, end=' ')
setc = seta - setb
for i in setc:
    print(i, end=' ')
dica = {}
dicb = {}
for i in range(n):
    try:
        dica[arr[i]] += 1
    except KeyError:
        dica[arr[i]] = 0
        dica[arr[i]] += 1
for i in range(m):
    try:
        dicb[brr[i]] += 1
    except KeyError:
        dicb[brr[i]] = 0
        dicb[brr[i]] += 1
#print(dica)
#print(dicb)
arr = list(dica.keys())
brr = list(dicb.keys())
brr.sort()
arr.sort()
for k in range(len(arr)):
    if binarysearch(arr[k]) and (dicb[arr[k]] != dica[arr[k]]):
        print(arr[k], end=' ')
print()
