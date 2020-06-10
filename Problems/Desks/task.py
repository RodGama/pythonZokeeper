# put your python code here
_class_students = []
_students = int(input())
_class_students.append(_students)
_students = int(input())
_class_students.append(_students)
_students = int(input())
_class_students.append(_students)
_desks = (_class_students[0] / 2
          + _class_students[1] / 2
          + _class_students[2] / 2)
_desks = ((int(_class_students[0]/2) + (_class_students[0] % 2 > 0))
         + (int(_class_students[1]/2) + (_class_students[1] % 2 > 0))
         + (int(_class_students[2]/2) + (_class_students[2] % 2 > 0)))
print(_desks)
