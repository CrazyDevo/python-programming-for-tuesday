day_number=45

day_name=None

if day_number==1:
    day_name="Monday"
elif day_number==2:
    day_name="Tuesday"
elif day_number==3:
    day_name="Wednesday"
elif day_number==4:
    day_name="Thursday"
elif day_number==5:
    day_name="Friday"
elif day_number==6:
    day_name="Saturday"
else:
    day_name="Sunday"


print(day_name)

print("----------------")

if day_number>=1 and day_number<=7:
    if day_number == 1:
        day_name = "Monday"
    elif day_number == 2:
        day_name = "Tuesday"
    elif day_number == 3:
        day_name = "Wednesday"
    elif day_number == 4:
        day_name = "Thursday"
    elif day_number == 5:
        day_name = "Friday"
    elif day_number == 6:
        day_name = "Saturday"
    else:
        day_name = "Sunday"

    print(day_name)
else:
    print("invalid day number")