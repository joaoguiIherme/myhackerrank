if __name__ == '__main__':
    lista = []
    new = []
    notas = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        new = [name, score]
        lista.append(new)
    
    for x in lista:
        notas.append(x[1])
    
    m = min(notas)
    while m in notas:
        notas.remove(m)
  
    n = min(notas)
    lista.sort()
    for y in lista:
        if y[1]==n:
            print(y[0])
