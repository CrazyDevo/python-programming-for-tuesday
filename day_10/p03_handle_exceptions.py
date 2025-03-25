name='Python Program'
try:
    print(name[20])
except:
    print("Error: Index out of range")

print("Adam")


try:
    print(9/1)
except:
    print("Zero Division Problem")
else:
    print("No error")


print("Adam")

try:
    print(9/0)
except:
    print("Zero Division Problem")
else:
    print("No error")
finally:
    print("This will always execute")