# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [1, 2, "shanvi", False]
print(mylist)
print(len(mylist))

# to access a member of a sequence type, use []
print(mylist[2])
print(mylist[-1])

# add a list to another list
anotherlist = [3, 4]
print(anotherlist)

# mylist = anotherlist + mylist
mylist = mylist + anotherlist
print(mylist)

mystr = "this is python" #immutable
print(len(mystr))
print(mystr[2])

# use slices to get parts of a sequence
print(mylist[1:4])
print(mylist[1:5:2])
print(mylist[::2])

# you can use slices to reverse a sequence
print(mylist[::-1])
print(mylist[:2:-1])
print(mystr[::-1])

# Tuples are like lists, but they are immutable
mytuple = (1, 2, "name", 0)
print(mytuple[1])

# Sets are also sequences, but they contain unique values
myset = {1, 2, 2, 3, 4, 2}
print(myset)

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(1 in mylist)
print(2 in mytuple)
print(3 in myset)