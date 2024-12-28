#EXCEPTION HANDLING IN PYTHON
#definition: Exception handling is a mechanism to handle runtime errors or exceptions in a program.
#It is used to handle the runtime errors and make the program more robust.
#There are two types of exception handling in python: try-except and try-except-finally

'''try-except block: It is used to handle the exceptions that may occur during the execution of
    the code in the try block. If an exception occurs in the try block, the code in
    the except block is executed'''
'''try-except-finally block: It is used to handle the exceptions that may occur during the
    execution of the code in the try block. If an exception occurs in the try block,
    the code in the except block is executed. The code in the finally block is executed
    regardless of whether an exception occurred or not.'''

try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:  #prints the error explicitly
    print(e)
    #this doesn't crash and the error is printed explicitly

print("Thank you!") #this is executed regardless of whether an exception occurred or not

#crashing code is undesirable

#we can also perform specific exception handling using specific exception types
'''
try:
    #code
except ZeroDivisionError as e:
    #code
except TypeError as e:
    #code
except as e:     #for any other error
'''

#We can also raise an error

a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
if b == 0:
    raise ZeroDivisionError("Cannot divide by zero!")
    #this gives a custom error
    #raise crashes the program.
    #its for the developer for critical errors
else:
    print(a/b)  #this will print the division of a and b


#try with else clause
#if try block successfully executed, only then the else block is executed, written after except block

#FINALLY clause
#The finally block is used to execute a block of code regardless of whether an exception was thrown or
#not. It is used to release any system resources that your program may be using.    

#it is useful in a function
print("FInally")
def main():
    try:
        a = int(input("Enter a number: "))
        return a    #would've ended the code block without finally

    except Exception as e: 
        return e
        
    finally:   #executes the code even if the function has return value above     
        print("I am inside finally")
    #finally executes regardless of whether an exception occurred or not

main()  #function call

