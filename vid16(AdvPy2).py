#VIRTUAL ENVIRONMENT
#used for creating an isolated environment for various packages
#installing packages in this environment will not affect the main environment

#command for virtual environment
# pip install virtualenv
# virtualenv venv
# venv\Scripts\activate
# deactivate

#FREEZE command -> shows all the packages and their version
# pip freeze

#pip freeze > requirements.txt -> stores all information in a file named requirements.txt

#LAMBDA function -> functions created using an expression using lambda keyword
#shorcut to create a function and assign it to variable

# printing a square easy func
square = lambda x: x**2
#thus takes arg x, and return x squared
print(square(5))

#JOIN method
#used for joining strings
list = ["Salman", "Khan", "Bollywood"]
print("-".join(list))   #joins the elements using - as a separator

#Q. Create a vertical table using join methods 
n = int(input("Enter a number: "))
table = (str(n*i) for i in range(1,11))
print("\n".join(map(str,table)))

#MAP, FILTER AND REDUCE
#MAP -> applies a function to each item in an iterable
#FILTER -> filters items from an iterable based on a condition
#REDUCE -> applies a function of two arguments cumulatively to the items of an iterable,
#from left to right, so as to reduce the iterable to a single output.

#map(function, iterable)
l = [1,2,3,4,5,6]
square = lambda x: x**2
sqlist = map(square, l)
# print(list(sqlist))

#FILTER
def is_even(x):
    return x % 2 == 0

l = [1,2,3,4,5,6]
even_list = filter(is_even, l)
# print(list(even_list))

#Reduce
def sum(a,b):
    return a + b
from functools import reduce    #needs to be imported
print(reduce(sum,l))

#Q. Write a function that returns the greatest if the list using reduce function
from functools import reduce
l = [121,34,45,556,27,928,2,4,55,2]

def greater(a,b):
    return a if a > b else b
print(f"The greater number is {reduce(greater,l)}")


