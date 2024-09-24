#******STRINGS*****
'''Strings are datatypes that store sequence of characters
    They are defined in single quotes, double quotes, and triple quotes as well'''

#Escape characters -> Special characters for formatting
'''\n -> for next line
   \t -> for space(tab)'''
print("Hello\nWorld")  # prints Hello and then on next line World
print("Hello\tWorld")  # prints Hello and then a tab space and then World

#String Concatenation
'''adds two strings'''
print("Hello" + "World")  # prints HelloWorld

#indexing: numbering particular characters in a string
str = "Hello World"
print(str[0])   #prints H
print(str[2])   #prints l
print(str[5])   #empty space

#we can oly access characters using string, not manipulate it
# thus str[1] = x is not possible i.e assignment

#Slicing ->  accessing a subset of string

'''Syntax:  str[ starting index : ending index]'''

#starting index is included while ending index is excluded 

word = "Vishnu"
print(word[0:4])  # prints Vish
print(word[1:4])  # prints his
print(word[:2])    #prints Vi
print(word[2:])     #prints shnu
print(word[3:len(word)])    #3rd index to last

#negative indexes
#-1 is last index, -2 is second last index and so on
print(word[-3:-1])
print(word[-6:-2])

#Some  string methods
#1. lower() -> converts string to lower case
#2. upper() -> converts string to upper case
#3. title() -> converts string to title case
#4. swapcase() -> swaps the case of string
#5. count() -> counts the number of occurrences of a substring
#6. .endsWith("xy")
#7. .startsWith("xy")
#8. .replace("old","new")
#9. .find(word)

print(word.replace("i","ee"))
print(word.endswith("nu"))

#Program to find length of inputted string
str = input("Enter a string: ")
print("The length of the string is ",len(str))

#CONDITIONAL STATEMENTS
#1. if statement
#2. if-else statement
#3. if-elif-else statement

age = int(input("Enter your age: "))
if(age<18):
    print("You are a minor")
elif(18 <= age  <= 60 ):
    print("You are an adult")
else:
    print("You are a senior citizen")

light = input("Enter light variable: ")
if (light == "red"):
    print("STOP")
elif(light=="green"):
    print("GO")
else:
    print("WAIT")
    
#Q. Grade Students based on their marks using If-else conditionals

marks = int(input("Enter your marks: "))

if(marks <= 90):
    grade = "A"
elif(90> marks>80):
    grade = "B"
elif(80 >=  marks > 70):
    grade = "C"
elif(70 >= marks > 60):
    grade = "D"
else:
    grade = "F"
print("Your grades are: ",grade)

#NESTING  OF IF-ELSE STATEMENTS
#writing if statement inside an if statement

age = int(input("Enter your age: "))
if(age < 18):
    if(age > 80):
        print("You are too old to drive!") 
    print("You can drive!")
else:
    print("You are minor")
    
#Q. Write a program to check whether a number is even or odd using if-else statement
number =  int(input("Enter a number: "))
if(number%2==0):
    print("The number is even")
else:
    print("Number is odd!")
    
#Q. Write a progra to find the greatest of three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if(num1>num2 and num1>num3):
    gnum=num1
elif(num2>num1 and num2>num3):
    gnum=num2
elif(num3>num1 and num3>num2):
    gnum=num3
print("The greatest number is : ", gnum)

#Q. Write a program to find if a number is a multiple of 7 or not
num = int(input("Enter a number: "))
if(num%7==0):
    print("The number is a multiple of 7")
else:
    print("The number is not a multiple of 7")



