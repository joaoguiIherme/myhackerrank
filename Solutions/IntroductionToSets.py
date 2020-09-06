def average(array):
    sum = 0
    for x in set(array):
        sum += x
    y = len(set(array))
    return (sum/y)    
