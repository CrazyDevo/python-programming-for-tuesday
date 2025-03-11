import  numbers
def hello_world():
    print("Hello World")
    print("Hello World")

hello_world()

print("----------------------")

def hello_person(name):
    print(f"Hello {name}")


hello_person("Adam")

print("----------------------")

def eligible_person(age:int):
    if age > 18:
        print("Eligible person")
    else:
        print("Not Eligible person")


eligible_person(21)

print("----------------------")

def find_max_number(num1: numbers.Number, num2: numbers.Number):
    if num1>num2:
        print(num1)
    elif num2>num1:
        print(num2)
    else:
        print("Numbers are equal")


find_max_number(3,7.0)