tuple1=(10,20,30)
tuple2=(40,50,60)
tuple3=tuple1+tuple2
print(tuple1)
print(tuple2)
print(tuple3)

tuple4=2*tuple1 + 3*tuple2
print(tuple4)

print(tuple4.count(40)) # we are able to learn the number of elements
print(tuple4.index(40))