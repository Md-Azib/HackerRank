for _ in range((int(input()))):
    n = int(input())
    ans = ((n % 1000000007) * (n % 1000000007)) % 1000000007
    print(ans)
