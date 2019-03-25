# Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.
#
# For example, the length of your array of zeros n = 10. Your list of queries is as follows:
#
#     a b k
#     1 5 3
#     4 8 7
#     6 9 1
# Add the values of k between the indices a and b inclusive:
#
# index->	 1 2 3  4  5 6 7 8 9 10
# 	[0,0,0, 0, 0,0,0,0,0, 0]
# 	[3,3,3, 3, 3,0,0,0,0, 0]
# 	[3,3,3,10,10,7,7,7,0, 0]
# 	[3,3,3,10,10,8,8,8,1, 0]
# The largest value is 10 after all operations are performed.
#
# Function Description
#
# Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the resulting array.
#
# arrayManipulation has the following parameters:
#
# n - the number of elements in your array
# queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.

# 5 3
# 1 2 100
# 2 5 100
# 3 4 100
# Sample Output
#
# 200
# Explanation
#
# After the first update list will be   100 100   0   0   0.
# After the second update list will be  100 200 100 100 100.
# After the third update list will be   100 200 200 200 100.
# The required answer will be 200.


n, m = map(int, input().split())
arr = [0 for i in range(n + 1)]
#print(arr)
for i in range(m):
    a, b, add = map(int, input().split())
    arr[a] += add
    if b + 1 <= n:
        arr[b + 1] -= add
m = 0
s = 0
for i in range(1, n + 1):
    s = s + arr[i]
    if s > m:
        m = s
print(m)
