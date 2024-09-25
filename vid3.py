#LIST AND TUPLES

#lists are equivalent of arrays in Python which is used to store mutiple type of data in one variable linearly

marks = [45,90,44,96,69,78,9]

#we can access elements of the list using their indexes
print(marks[1])
print(marks[4])

info = ["karan",45,True,3.14]   #mutiple datatypes stored in one variable

#Note: STRINGS ARE IMMUTABLE IN PYTHON WHILE LISTS ARE MUTABLE(changeable)!

print(info[0])
info[0] = "Arjun"   #value changed 
print(info[0])

#List slicing - similar to string slicing

#Syntax: list_name[starting_idx : end_idx]    (ending idx excluded)

print(marks[1:4])   #prints 1 to 3 idx
print(marks[:4])   #prints 0 to 3 idx
print(marks[1:])   #prints 1 to end idx

#LIST METHODS

marks.append(34)    #adds element at end (mutating)
marks.sort()    #sorts in asc order
marks.sort(reverse=True)    #sorts in descending order
marks.insert(1, 34)    #inserts element at specified index
marks.reverse()     #reverse the list (mutating )
marks.pop(2)    #returns value at 2nd index
#most of the lists methods do not return new list rather make changes in the original list

#TUPLES IN PYTHON
#tuples are built in datatype used to create IMMUTABLE  sequence of characters

tup = (45,3,4,66,76,45)     #written in round bracket

#tuples can be accessed using indexes but we can modify them
print(tup[0])

tup1 = ()   #an empty tuple
tup2 = (2,)     #tuple with single value is written with a comma
tup.index(4)    #returns the index where 4 occurred for the first time
tup.count(76)   #returns the number of occurences

#Q. Write a program to ask user the names of their 3 favorite movies and store them in a list

'''mov1 = input("Enter your first favorite movie: ")
mov2 = input("Enter your second favorite movie: ")
mov3 = input("Enter your third favorite movie: ")

movies = []
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)'''

#Q. Write a program to check if a list contains a palindrome of elements.

mylist = [34,33,"chetan",33,34]

def is_palindrome(lst):
    templist = lst.copy()
    templist.reverse()
    if(templist==lst):
        print("It is Palindrome")
    else:
        print("It is not a Palindrome")

val = [1,2,1]
is_palindrome(mylist)
is_palindrome(val)
        

