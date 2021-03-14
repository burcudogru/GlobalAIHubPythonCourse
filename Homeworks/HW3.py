students= {"Name and Surname":[], "midterm": [], "project": [], "final": [], "passingGrade": []}
grades=""

for i in range (5):
    names= input("Name and Surname ")
    students["Name and Surname"].append (names)
    n1= float(input("midterm "))
    students["midterm"].append(n1)
    n2= float(input("project "))
    students["project"].append(n2)
    n3= float(input("final "))
    students["final"].append(n3)
    students["passingGrade"].append((0.3*n1)+(0.3*n2)+(0.4*n3))

for k,v in students.items():
    if (k=="passingGrade"):
        grades= v

grades.sort()
grades.reverse()
print(grades)

