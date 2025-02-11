# I will print the numbers from 1 to 10 and if I see 5 then I will exit the loop
for i in range(1,11):
    print(i)
    if i == 5:
        break

print("Loop ended")


# s=ABCDEFGHIJKLMNOPQRSTUVWXYZ when I see  E then I will exit the loop
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for each in s:
    print(each)
    if each == 'E':
        break


print("--------------------------------")


# I want to print the numbers from 1 to 100 and I want to skip the numbers if the number is divisible by 5 and I want to skip the numbers
# use continue statement
for i in range(1,101):
    if i % 5 == 0:
        continue
    print(i)

print("--------------------------------")

for i in range(1,10):
    # I will implement later
    pass

print("--------------------------------")

print(10)

