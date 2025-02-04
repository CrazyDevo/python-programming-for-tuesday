s='CYDEO'
print(len(s)) #number of characters

# forward indexes 0 1 2 3 4 5 6 ...
# backwards indexes  ... -5 -4 -3 -2 -1

print(s[0]) # get the first  character
print(s[-1]) # get the last character


print('----------------------------------------------------------------')
sentence="Python Programming Language"
#slicing string
          #           not included
# string[start index:end index]
print(sentence[0:6])

print(sentence[-8:])

print('----------------------------------------------------------------')
print(sentence[:6])

print(sentence[7:])

print('----------------------------------------------------------------')
word="ABCDEFGHJIKLM"

reversed=word[::-1] # reverse word

print(reversed)
print(word[-3:])