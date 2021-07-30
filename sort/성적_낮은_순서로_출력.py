# 이것이 코딩테스트다 - 성적이 낮은 순서로 학생 출력하기

n = int(input())
student_score = []
for _ in range(n):
    student_score.append(tuple(input().split()))


student_score.sort(key=lambda student_score: student_score[1])

for student in student_score:
    print(student[0], end=' ')
