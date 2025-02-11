s="Cydeo School"

for each  in s:
    print(each)

print("--------------------------------")

for i in range(1,101):  #the second parameter is not included
    print(i)

#print the sum of numbers from 1 to 20 1 + 2 + 3 + 4 + 5 .... +20
print("--------------------------------")
sum=0

for i in range(1,21):
    sum+=i

print(sum)

# print the even numbers from 1 to 100  2 4 6 8 10 .... 100


print("--------------------------------")

for i in range(1,101):
    if i % 2 ==0:
        print(i)

print("--------------------------------")
for i in range(2,101,2)      :  #2 4 6
    print(i)