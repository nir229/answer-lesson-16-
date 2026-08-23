grades = {}
grades['math'] = int(input('math grade: '))
grades['english'] = int(input('english grade: '))
grades['literature'] = int(input('literature grade: '))
grades['python'] = int(input('python grade: '))
print(grades)

avg_grades = sum(grades.copy().values()) / len(grades)
max_grade = max(grades.copy().values())
min_grade = min(grades.copy().values())

grades.update({"avg" : avg_grades, "max" : max_grade, "min" : min_grade})
print(grades)

del grades['literature']
print(grades)