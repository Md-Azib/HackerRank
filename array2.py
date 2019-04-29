def mergeSort(arr, n):
    if n > 1:
        mid = n // 2
        first = arr[:mid]
        last = arr[mid:]
        mergeSort(first, len(first))
        mergeSort(last, len(last))
        c = merge(arr, first, last)
        return c


def merge(arr, first, last):
    print(first)
    print(last)

    i, j, k = 0, 0, 0
    count = 0
    while i < len(first) and j < len(last):
        if first[i] <= last[j]:
            arr[k] = first[i]
            i += 1
        else:
            count += len(first) - i
            arr[k] = last[j]
            j += 1
        k += 1
    while i < len(first):
        #count += len(first) - 1

        arr[k] = first[i]
        k += 1
        i += 1
    while j < len(last):
        arr[k] = last[j]
        #count += len(first) - i
        k += 1
        j += 1
    return count


n = int(input())
arr = list(map(int, input().split()))

count2 = mergeSort(arr, n)
print(arr)
print(count2)