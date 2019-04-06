r, c = map(int, input().split())
dic = {}
dic[2] = [0, 2, 4, 6, 8]
dic[1] = [1, 3, 5, 7, 9]
x = 0
if r == 1:
    print(dic[2][c - 1])
elif r == 2:
    print(dic[1][c - 1])
else:
    if r % 2 != 0:
        x = (r // 2) * 10
    else:
        x = ((r - 1) // 2) * 10
    x += dic[(r % 2) + 1][c - 1]
    print(x)
