r, c = map(int, input().split())
print((r + r % 2) * (c + c % 2) // 4)
