
def hailstone(n):
    l = []
    while n != 1:
        l.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    l.append(n)
    return l

def hailstone_dict(n):
    hss = {}
    for i in range(1,n+1):
        hss[i] = hailstone(i)
    return hss

print(sorted(hailstone_dict(1000000).items(), key=lambda x: len(x[1]))[-1])