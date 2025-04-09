class Person:
    def __init__(self,name,age): # like constructor
        self.__name=name # protected
        self.__age=age # protected
    def get_name(self):
        return  self.__name

    def get_age(self):
        return self.__age

    def __str__(self):   #like toString()
        return f"{self.__name} - {self.__age}"

person=Person("Adam",36)
print(person.get_name())
print(person.get_age())

print(person)