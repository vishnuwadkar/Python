#----------------ADVANCED PYTHON--------------------

#WALRUS operator
#The walrus operator is a new feature in Python 3.8 that allows you to assign 
#values to variables in a conditional statement. It is called the walrus operator
#because it looks like a walrus with its tusks.
#The walrus operator is denoted by the := operator.

if (n := len([4,5,3,4]))>3:     #here, len of list will be assigned to n
    print(f"list has {n} elements, expected less than 3")
else:
    print(f"list has {n} elements which are ideal")

#TYPE DEFINITION IN PYTHON
#Python is a dynamically typed language, which means that you don't need to declare the type of
# a variable before using it. However, you can use type hints to specify the type of a
# variable, which can make your code more readable and self-documenting.
#hints are added using semi colon (:) after the variable name and (->) 
# after the variable name to specify the return type of a function.

n: int = 5  #thus we can now use all methods of integer by explicitly declaring it int
print(n)  # Output: 5
name: str = "John"  #thus we can now use all methods of string by explicitly declaring it string
print(name)  # Output: John

def sum(a: int, b: int)-> int:  #this means, sum takes a as int and b as int and then returns int(->)
    return a + b

#thus type definition is not mandatory but it is good practice to use it for better readability and understanding of the code.

#Advanced Type Hints
from typing import List, Dict, Tuple, Union

#List is a type hint for a list of elements
numbers: List[int] = [1, 2, 3, 4, 5]

#Tuple of a string and an int
person: Tuple[str, int] = ("John", 30)

#Dictionary with string keys and int values
person: Dict[str, int] = {"name": "John", "age": 30}

#Union type for variables that can hold multiple types
#Union is used to specify that a variable can hold multiple types.
identifier: Union[int,str] = "ID234"

#MATCH CASE
#The match-case statement is a new feature in Python 3.10 that allows you to write
#more readable and concise code for handling multiple cases.
#The match-case statement is similar to the if-elif-else statement, but it is more
#concise and easier to read and understand.
#The match-case statement is used to handle multiple cases, and it is similar to the if-elif-else statement.

def httpStatus(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _ :        #anything else
            return "Unknown Status"

print(httpStatus(404))
print(httpStatus(500))
print(httpStatus(302))
print(httpStatus(200))

#GLOBAL keyword
#The global keyword is used to indicate that a variable is global, and it is not local to
#the function or block where it is used.
x = 10  #this is a global variable
def func():
    global x  #this indicates that x is a global variable
    x=3 #this changes the global variable x
    print(x)  #prints 3

print(x)  #prints 3
func()  #also prints 3

#ENUMERATE  FUNCTION
#The enumerate function is used to iterate over a list (such as a string, tuple, list
#or any other iterable) and return both the index and the value of each item in the list
#The enumerate function returns an enumerate object, which is an iterator that produces
#tuples, where the first item is the index and the second item is the value of each
#item in the list.
#The enumerate function is useful when you need to iterate over a list and also need
#to know the index of each item in the list.
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
    #OUTPUT: 0 apple, 1 banana, 2 cherry

#LIST COMPREHENSION
#List comprehension is a feature in Python that allows you to create lists in a more
#concise way than using a for loop.
#List comprehension is a compact way to create lists from existing lists or other iterables.
#The basic syntax of list comprehension is as follows:
# [expression for variable in iterable if condition]

myList = [1, 2, 3, 4, 5]
squaredList = [x*x for x in myList]
print(squaredList)  #OUTPUT: [1, 4, 9, 16, 25]

#print table using list comprehension
n = int(input("Enter a number: "))
print([n*i for i in range(1, 11)])  #prints a table of numbers from 1 to 10



