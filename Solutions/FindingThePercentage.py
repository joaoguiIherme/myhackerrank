if __name__ == '__main__':
    n = int(input())
    total = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    x = (student_marks[query_name])
    for v in x:
        total += v
    answer = total/3
    print("{:.2f}".format(answer))
