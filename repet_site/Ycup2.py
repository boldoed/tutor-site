def poisk(h, s):
    sp = []
    for l in range(len(s)):
        for r in range(l+h, len(s), h):
            sr = s[l:r]
            if sr == sr[::-1]:
                sp.append(sr)
    if sp != []:
        return min(sp)
    return 0

s = input()
for h in range(2, len(s)):
    find = poisk(h,s)
    if find != 0:
        print(find)
        break
    if h == len(s) - 1:
        print(-1)