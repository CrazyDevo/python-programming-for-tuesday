from day_11.inheritance.parent import Person


class Student(Person):
    pass


student=Student("Adam",36)

print(student.name)
print(student.age)