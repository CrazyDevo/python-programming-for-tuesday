number=int( input("Enter the number to check positive or negative or zero:\n"))


if number>0:
    print("The number is positive")
elif number<0:
    print("The number is negative")
else:
    print("The number is zero")


print("----------------------------------------------------------------")

result=None
if number>0:
    result="Positive"
elif number<0:
    result="Negative"
else:
    result="Zero"

print(result)

