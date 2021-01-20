def lineUp(n, students):
    students.sort(key=lambda x: (-x[0], -x[1]))
    for student in students:
        print(student[0], student[1], student[2])


n = int(input())
students = []
for i in range(n):
    t, w = input().split()
    t, w = int(t), int(w)
    students.append((t, w, i+1))
lineUp(n, students)
