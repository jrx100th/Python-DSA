"""
Classes

every data structure are created using classes



class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

cookie_one = Cookie('green')

# cookie_one is a variable name
# and we are setting it to be type cookie 
# and when we pass the color green for the cookie then attribute is green for the cookie

cookie_two = Cookie('blue')
# another cookie with color attribute as 'blue'

print('cookie one is', cookie_one.get_color())
print(f"cookie two is {cookie_two.get_color()}")

cookie_one.set_color('yellow')


print('cookie one is', cookie_one.get_color())
print(f"cookie two is {cookie_two.get_color()}")


# since every data structure is an object and are from a class

# like this

class LinkedList:

    def __init__(self):
        pass
    def append(self, value):
        pass
    def pop(self):
        pass
    def prepend(self, value):
        pass
    def insert(self, index, value):
        pass
    def remove(self, index):
        pass

#   so we are going to use these functions to perform operations on the data structure
"""

"""
Pointers

"""
num1 = 11
num2 = num1

# checking where num2 is pointing towards

print("Before num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

print("\nnum1 points to :", id(num1))
print("num2 points to :", id(num2))

# damn they are referencing the same id(memory location/address)

num2 = 22

print("\nAfter num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# num2 location is changed

# integers are immutable and cannot be changed so a new location is allocated



dict1 = {
    'value' : 11
}

dict2 = dict1

# now both are going to point at the same dictionary and same location

dict2['value'] = 22

print(dict1) # now this value is changed and dict1 'value' is showing 22

# even the location doesnt change and points in the same location
# and since they point to the same location 
# they both will show the same value


# integers are immutable and cant be changed
# dictionaries can be changed

# Eg: nodes in a linked list will operate similarly to a dictionary(pointing)

# @dictionaries we can change where that are pointing towards

dict3 = {
    'value':33
}

dict2 = dict3

dict1 = dict3

# now all the dictionaries are pointing towards the location of dict3

# now what happens to the dictionary when we created dict1

# since no entity is pointing towards the dictionary in dict1

# python's garbage collection will remove this with a process called garbage collection