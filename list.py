my_list = []

#adding elements using append
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


print("After Append:", my_list)

my_list.insert(1, 15)

#adding two lists using extend
my_list.extend([50, 60, 70])

#remove last element

my_list.pop()

print("After Pop:", my_list)

#sort list in ascending order

my_list.sort()
print("After Sort:", my_list)

# find index of 30

my_list.index(30)


