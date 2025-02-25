"""
Big O : Intro

comparing code mathematically on how effeciently it runs

time complexity - measured in no of operations that it takes to complete something

space complexity - memory space
"""

"""
Big O: Worst case
omega 
theta
o - omekron

best case scenario - omega - completing in one operation
Average case - theta - middle
worst case scenario - O - completing after max number of possible operations

"""

"""
Big O: O(n)

O(n)

def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

# so here n is the number of operations
"""

"""
Big O: Drop Constants

Simplifying Big O notation



def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)
# this ran n+n times -> 2n -> drop constants -> O(n)
"""

"""
Big O: O(n^2)


def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)

# n*n = n^2 items were printed --> O(n^2) --> steeper line
# O(n^2) = less effecient from a time complexity standpoint
"""

"""
Big O Drop non dominants


def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
        # o(n**2)
    for k in range(n):
        print(k)
        # o(n)

        # total = O(n**2 + n)
        # compared to the n**2, n is a very small term....non dominant term
        # so after dropping non dominants (n)
        # final is O(n**2)


print_items(10)
"""

"""
Big O: O(1)


def add_items(n):
    return n+n
    # now you have only one operation
    # that is O(1)

    # O(1) --> constant time even if the value increases
    # flat line
    # Most effecient
"""


"""
Big O: O(log n)

# sorted data 
# finding the most effecient way to look for a number in this list
# list of 8 elements - [1,2,3,4,5,6,7,8]
# cutting it in half and checking for 1
# in 3 steps we will get 1
# 2^3 = 8
# log base2 8 = 3
# so it takes 3 steps to cut it down to a single item in an list of 8 elements
# this is O(log n)

# this is more effecient than O(n2) and O(n)
# but not effecient than 0(1)

# so it is second most effecient Big O


# O(nlog n) - some sorting algorithms - merge,quick - strings,etc
"""

"""
Different terms for inputs

def print_items(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)
    
    now it will be O(n+n) = O(2n)
    # which will be o(n)

# but for 

def print_items(a,b):
    for i in range(a):
    print(i)

    for j in range(b):
    print(j)

    # now the Big O will be considering both the parameters a and b
    O(a + b)



de print_items(a,b):
    for i in range(a):
        for j in range(b):
        print(i,j)

        # now for this nested for loop the complexity will be
        # O(a * b)
"""

"""
Big O of lists


my_list = [11,3,23,7]

print(my_list)

my_list.append(17)

print(my_list)

my_list.pop()

print(my_list)

# this above operation such as append or pop is a single operation and 
# has complexity of O(1)


# popping the element at the first index 
# then we need to reindex everything
my_list.pop(0)

print(my_list)

# inserting 11 at the index 0 
# so after inserting then we need to reindex everything
my_list.insert(0,11)

print(my_list)

# so for reindexing everything the complexity is O(n)
# n is the number of elements in the list

# removing or adding at the end of the list is O(1)
# removing or adding at the start of the list is O(n)

# even if we insert or remove from the middle of a list
# it wont be O(1/2n)
# it will be O(n) --> dropping constants
# and Big O will only see for the worst case O(n) not the average case O(1/2n)


# searching for a "value" in a list 
# if we search for 7 in the list then the complexity will be O(n)... as it is in last

# but if we search for a index....index are in memory
# so if we do it by index then it will be 0(1)...directly in the memory
"""

"""
Big O: Wrap up

when n = 100

O(1) = 1
O(log n) = approx(7)
O(n) = 100
O(n**2) = 10000

when n = 1000

O(1) = 1
O(log n) = approx(10)
O(n) = 1000
O(n**2) = 1000000

O(n2) to O(n)

O(n2) = loop within a loop

O(n) = proportional, a always a straight line

O(log n) = divide and conquer

O(1) = constant time

All the space complexity is going to be the same for all the data structures except for the skip list


Array sorting algorithms - different

"""