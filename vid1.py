print("Hello World!")
#prints hello world!
#here print is a function

#Variables in python!
#Variable are names given to memory location in a program
name = "Vishnu"     #here 'name' is  a variable
age = 20

print(name)     #printing using variable name
print(age)

print("My name is: ", name, "and my age is ",age)     #printing using variable name with string

# assigning values to variables
age2 = age
#thus age's value is assigned to age2 variable

#type fucntion: returns type of a variable
print(type(age))    #int
print(type(name))   #str(string)

#printing sum using variables
a=2
b=4
sum = a+b
print(sum)

#assignment operators in python
num = 10
num = num + 2
#now value of num becomes 12 i.e 10 + 2

#this can be simplified using special operator: +=
num1 = 10
num1+=2
print(num1)

#similarly we can also use  -=, *=, /=, %=, **=, //=, <<=, >>=, &=, ^=

#type conversion and type casting
#type conv is automatic while typecasting is manual

#consider two different type of variables
a=2     #int
b=4.5   #float

sum = 2 + 4.5   # 2.0 + 4.5 = 6.5
#here python automatically converts int to float
print(sum)

#type casting
#converting float to int 
x= 4.5 #a float
y = int(x)  #float converted to int

a = 3.14
a = str(a)      #now 'a' is a string converted from float 

#taking input from user
name = input("Enter your name: ")   #displays on terminal
x = int(input("Enter your number:  "))  #takes number as input
print("Welcome ", name, "and you have entered number ",x) 

#NOTE:  input() function always returns string. If you want to take number as input, you need to convert 


#Practice Question: Write a program to enter two numbers and print their sum

fnum = int(input("Enter first number: "))
snum = int(input("Enter second number: "))
print("Sum of two numbers is: ", fnum+snum)  #sum of two numbers

#Write a program to input side of a square and print its area
side = int(input("Enter the side of cube: "))
area = side**2
print("Area of square is: ", area)  #area of square

#Write a program to input two floating numbers and calculate their avg
p = float(input("Enter first number: "))
q = float(input("Enter second number: "))
avg = (p+q)/2
print("The average is : ", avg)  #average of two numbers

#Write a program to input two numbers and print True if a is greater than or equal to b or else print false
v = int(input("Enter first no: "))
w = int(input("Enter second no: "))
print(v >= w)






