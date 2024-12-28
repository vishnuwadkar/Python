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



