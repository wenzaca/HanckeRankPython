if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum_grade = 0.00
    grades = student_marks.get(query_name)

    for grade in grades:
        sum_grade += grade

    avg_grade = float(sum_grade) / len(grades)

    print ('%.2f' % (avg_grade))
