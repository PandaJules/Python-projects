from collections import Counter
from collections import namedtuple

heights = [170, 170, 169, 152, 170, 169, 158, 188, 142, 168, 171, 158]
print(Counter(heights))
print(Counter(heights).items())
print(Counter(heights).keys())
print(Counter(heights).values())

Student = namedtuple("Student", "MARK, NAME, ID")
students = [Student(90, "Jake", "J13"), Student(79, "Tony", "T44"), Student(83, "Matt", "M24")]
average = sum(stud.MARK for stud in students)/len(students)
print(average)