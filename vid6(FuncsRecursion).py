#FUCNTIONS AND RECURSION

#functions are block of statement that perform a specific task
#def keyword is used to define a function

def sum(a,b):   #function definition
    add = a+b   #work
    return add  #return value

x=3
y=5
print(sum(x,y)) #function call
print(sum(300,876)) #function call
print(sum(19,4)) #function call

#thus functions reduces redundancy in code

def greet(name):
    print("Hello ",name)    #function that returns nothing (None)

greet("Vishnu")
greet("Harry")

#Write a function that calculates the average of three numbers
def average(a,b,c):
    avg = (a+b+c)/3
    return avg

print(average(10,20,30)) #function call
print(average(199,234,1000)) #function call
print(average(23,43,45)) #function call

#the print function
# print(value,separator,end) -> an in build function
# print() function is used to print the value in the console
print("Hello","Lentgh",end=" ",sep="$",)  #by default end is \n which is next line but by passing end arg we change it
print("Hello")  #thus the two hello's will be printed on the same line
# f string is used to pass a variable in a string
name = "Vishnu"
print(f"Hello {name}, How are you?!")

#there are two types of functions in Python
#1. built in functions
#2. user defined functions

#DEFAULT PARAMETERS - values that will be used if we pass no argument
def greet(name="Nobody"):
    print("Hello ",name)    #function that returns nothing (None)
greet() #no argument passed

#Practice Questions
#write a function to print the length of the list
def length(lst):
    return len(lst)
print(length([1,2,3,4,5,6,7,8,9]))

#write a function to print elements of list in a single line
def prnt_list(list):
    for el in list:
        print(el,end=" ")
    print()

lst = [1,2,3,4,5,6,7,8,9]
prnt_list(lst)

#Write a function to write a factorial of n

def fact(n):
    f=1
    for  i in range(1,n+1):
        f*=i
    print(f)

fact(3)    
fact(10)    
fact(5)    

#Write a function to convert USD to INR
def conv(usd):
    print("USD :",usd,"->  INR: ",usd*83)

conv(100)
conv(84)
conv(2000)

#write a function that takes an input number and prints if its odd or even
"""def odd_even():
    n=int(input("Enter number: "))
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")"""

# odd_even()  #function call

#RECURSION
# When a function calls itself repeatedly

#Print numbers from n to 1
def show(n):
    if n==0:
        return
    print(n)
    show(n-1)   #function called in itself i.e recursion    

show(5)     #recursive function call

#Finding factorial using recursion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print("Factorial of 5 is : ",fact(5))
# print("Factorial of 5 is : ",fact(300))
print("Factorial of 5 is : ",fact(10))

# Q. Write a recursive function to calculate sum of first n natural numbers

def rsum(n):
    if n==0:    #base condition
        return 0
    else:
        return n+rsum(n-1)

print("Running sum of 3: ",rsum(3))
print("Running sum of 5: ",rsum(5))

#Q. Write a recursive function to print all elements in a list
def print_list(lst,idx=0):
    if idx == len(lst):     #base condition
        return
    else:
        print(lst[idx],end=" ")
        print_list(lst,idx+1)   #recursion

mylist = ["Start",56,34,22,11,876,44,32,4,66,78,343,"End"]
print_list(mylist)