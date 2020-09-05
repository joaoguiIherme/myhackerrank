def solve(s):
    x = []
    s = list(map(str, s.split(' ')))
    for i in s:
        x.append(i.capitalize())
    return(' '.join(x))
    