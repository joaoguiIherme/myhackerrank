if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new = list(arr)
    x = max(new)

    while x in new:
        new.remove(x)
    
    print(max(new))
