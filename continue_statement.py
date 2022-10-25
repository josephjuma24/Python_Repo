i = 0
s = 'FOSSTechNix'
while i < len(s):
    if s[i] == 'T' or s[i] == 'S':
        i += 1
        continue
    print(s[i])
    i += 1