while True:
    h, m = map(int, input().split())
    nh, nm = 0, 0
    if h == 0 or h == 6:
        nh = h
    elif h > 6:
        nh = 12 % h
    else:
        nh = 12 - h
    if m == 0 or m == 60:
        nm = m
    elif m > 30:
        nm = 60 % m
    else:
        nm = 60 - m
    print(nh, nm)