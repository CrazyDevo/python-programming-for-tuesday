class MyClass:
    x=5

    def my_method(self,name):
        print(f"Hello {name}")


first_class=MyClass()
print(first_class.x)

print(first_class.my_method("Adam"))
