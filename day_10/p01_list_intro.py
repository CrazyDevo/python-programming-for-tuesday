groceries_list=['Eggs','Apples','Banana','Cherry']

print(type(groceries_list))

print(len(groceries_list))

print(f"Before : {groceries_list}")

groceries_list.append("Milk")

print(f"After : {groceries_list}")

print(groceries_list[-1])

sub_list=groceries_list[0:3]

print(f"Sub list : {sub_list}")

last_two=groceries_list[-2:]

print(f"Last two : {last_two}")

print("--------------------------------")

for each in groceries_list:
    print(each)

print("--------------------------------")
list1=['A','B','C']
list2=['D','E','F']

merged_list=list1*2+list2

print(merged_list)