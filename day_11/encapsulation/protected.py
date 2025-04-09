class Person:
    def __init__(self,name,age): # like constructor
        self._name=name # protected
        self._age=age # protected
    def get_name(self):
        return  self._name

    def get_age(self):
        return self._age

    def __str__(self):   #like toString()
        return f"{self._name} - {self._age}"

person=Person("Adam",36)
print(person.get_name())
print(person.get_age())

print(person)