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
        k += 1
        j += 1
    #print(arr)
    #print("Count is : {}".format(count))

    # while k < len(first) + len(last) - 1:
    #     print('in while loop')
    #     #print(i, j, k)
    #     print(first[i])
    #     print(last[j])
    #     if first[i] >= last[j] or j == len(last):
    #         arr[k] = first[i]
    #         i += 1
    #     elif first[i] < last[j] or i == len(first):
    #         count += len(first) - i
    #         arr[k] = last[j]
    #         j += 1
    #     k += 1
    #print(arr)
    return count


n = int(input())
arr = list(map(int, input().split()))
count2 = mergeSort(arr, n)
print(count2)