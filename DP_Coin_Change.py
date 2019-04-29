cost = [[0 for i in range(250)]for j in range(50)]
def count(n, m):
    if n < 0 or m <= 0:
        return 0
    if n == 0:
        return 1


n, m = map(int, input().split())
arr = list(map(int, input().split()))
