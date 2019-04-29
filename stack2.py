queue = []
stack = []
for _ in range(int(input())):
    values = list(map(int, input().split()))
    if values[0] == 1:
        queue.append(values[1])
        stack.append(values[1])
    elif values[0] == 2:
        queue.pop(0)
        stack.pop(-1)
    elif values[0] == 3:
        print(queue[0])
