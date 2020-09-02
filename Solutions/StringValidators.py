if __name__ == '__main__':
    s = input()
    y1 = False
    y2 = False
    y3 = False
    y4 = False
    y5 = False

    for x in range(0, len(s)):
        if s[x].isalnum():
            y1 = True
        if s[x].isalpha():
            y2 = True
        if s[x].isdigit():
            y3 = True
        if s[x].islower():
            y4 = True
        if s[x].isupper():
            y5 = True
    print(y1)
    print(y2)
    print(y3)
    print(y4)
    print(y5)
