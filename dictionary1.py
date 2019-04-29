n, m = map(int, input().split())
magazine = input()
note = input()
magazine = magazine.split()
note = note.split()
mag = {}
notes = {}
for i in magazine:
    try:
        mag[i] += 1
    except KeyError:
        mag[i] = 1
flag = False
for i in note:
    try:
        if mag[i] == 0:
            flag = True
            break
        else:
            mag[i] -= 1
    except KeyError:
        flag = True
        break
if flag:
    print('No')
else:
    print('Yes')
