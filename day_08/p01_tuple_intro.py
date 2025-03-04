days=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(type(days))
print(days[0])
print(days[1])
print(days[2])
print(days[-3])
print(len(days))
print("--------------------")

for each in days:
    print(each)

print("--------------------")
working_days=days[:5]
print(working_days)

print("--------------------")
# weekends=days[5:]
weekends=days[-2:]
print(weekends)

# days[1]="Adam" # YOU CAN NOT DO THIS
print("--------------------")
tuple4=(45,"Adam",'M',True,('M',True))

print(tuple4)