n=int(input())

array=[]
for i in range(n):
    input_d=input().split()
    array.append((input_d[0], int(input_d[1])))

array=sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
