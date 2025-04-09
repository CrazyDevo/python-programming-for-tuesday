class Person:
    def __init__(self,name,age): # like constructor
        self.name=name
        self.age=age
    def __str__(self):   #like toString()
        return f"{self.name} - {self.age}"

person=Person("Adam",36)
print(person.name)
print(person.age)

print(person)