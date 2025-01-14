# string + string
print("Adam is " + "the best candidate for the instructor")


# string + variable
name = "Adam"
county="Turkey"
age=34

print("My name is " +name)
print('I am from ' +county)
# print("I am " + age+ " years old")
print("I am " + str(age)+ " years old")

# format method to concatenate
print("----------------------------------------------------------------")
print("I am {} years old".format(age))
print("I am {} years old and I am from {}".format(age, county))

# f-strings to concatenate
print("----------------------------------------------------------------")
print(f" I am {age} years old and I am from {county}")
