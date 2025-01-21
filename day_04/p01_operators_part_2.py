# Relational Operators
from day_02.p02_variables import is_eligible

n1 = 100
n2 = 200

print(n1 < n2)
print(n1 > n2)

print("--------------------------------")
a = 100
b = 100

print(a >= b)
print(a <= b)

print("--------------------------------")

x = 100
y = 200
z = 100

print(x == y)  # False
print(x == z)  # True
print(x != y)  # True

print("--------------------------------")

word1='Python'
word2='Python'

print(word1 == word2)



print("-----------LOGICAL OPERATORS------------------")
# Logical Operators

age=16
is_usa_citizen=True

is_eligible_to_vote=age >=18 and is_usa_citizen

print(is_eligible_to_vote)


print("--------------------------------")

grade='F'

passed_exam=grade == 'A' or grade == 'B' or grade == 'C'

print(f"PASSED = {passed_exam}")

failed_exam=grade = not passed_exam

print(f"FAILED = {failed_exam}")

print("--------------------------------")
# Membership Operators

sentence="I know programming languages like Python , Java , Javascript , Kotlin, Scala, Groovy"

has_python='Python' in sentence

print(f"Has Python = {has_python}")

has_not_typescript='Typescript' not in sentence

print(f"Has not TypeScript = {has_not_typescript}")




