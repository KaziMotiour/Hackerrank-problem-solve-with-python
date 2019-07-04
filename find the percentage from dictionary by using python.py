n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
raw_data=input()
list=list(student_marks[raw_data])
b=0
c=0.0
for i in range(len(list)):
            b+=list[i]
            c+=1.0
print("{0:.2f}".format(b/c))
