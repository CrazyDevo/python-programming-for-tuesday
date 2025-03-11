


def square(number:int):
    return number*number


print(square(10))

def cube(number:int):
    return number*number*number

print(cube(10))

print("----------------")

def cube2(number:int):
    return number*square(number)


print(cube2(10))

print("----------------")

def multiply(num1:int=1,num2:int=1):
    return num1*num2


print(multiply(10,12))