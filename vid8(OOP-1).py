#To map with real world scenarios, we started using objects in code
#This is called as Object  Oriented Programming (OOP)

#CLASS AND OBJECT
'''Class is the blueprint(template) for an object while an object is the 
    instance of the class'''

#creating a class
class Student:
    name = "Vishnu"

#creating an object of class
myobj = Student()
print(myobj.name)

obj2 = Student()    #another object of the same class
print(obj2.name)

'''class Car:
    color = "blue"
    type = "Hatchback"

Lexus = Car()
print(Lexus.color)
print(Lexus.type)'''

#CONSTRUCTOR - a special function defined as __init__() func, which is always executed when the class is initiated

class Bacche:
    def __init__(self):     #constructor syntax
        #here self is the location of the object
        print("Adding new student...")
        print(self)
    name = "Kuch bhi"

Kid = Bacche()
print(Kid.name)

#Passing parameters
class stud2:
    def __init__(self, name, age):  #self can be named anything, but usually written as self
        self.name = name    #self refers to the object itself
        self.age = age      #this is an instance attr which is diff for every object of the class 
    college = "ABC College"     #this is a class attribute which is stored only once in the memory and is common to all objects

myStud = stud2("Vishnu",20) #passing arguments
print(myStud.name)
print(myStud.age)

print(stud2("xyz",21).name)

# METHODS: methods are functions that belongs to the objects 

class Boys:
    def welcome(self):  #for every method, self is a mandatory para, even if it takes no arg
        print("Welcome to the class, Boys!")
    def intro(self,name,marks):
        print(f"Hello, my name is {name} and I scored {marks} marks")

boy1 = Boys()   #obj creation
boy1.welcome()  #method call
boy1.intro("Vishnu",78)

boy2 = Boys()   #obj creation
boy2.welcome()  #method call
boy2.intro("Harry",80)

class myStud:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum=0
        for i in self.marks:
            sum = sum + i
        avg = sum/len(self.marks)
        return  avg


    
s1=myStud("Tony Stark",[90,56,78])
print(s1.avg())

#STATIC METHOD
#when we don't have to use the self parameter
#works at class level
class myStud:
    @staticmethod   #decorator for static method
    def hello():    #no self para reqd
        print("Hello, I am a static method!")
#Prac Que: Write a program to anage the account details, credits and deposits of the account

class Account:
    def __init__(self,no):
        self.acc_no = no
    
    balance = 0
    
    def  credit(self,amt):
        self.balance = self.balance + amt
        print(f"Amount credited to account {self.acc_no} successfully! Available balance: {self.balance}")
    
    def debit(self,amt):
        if self.balance >= amt:
            self.balance = self.balance - amt
            print(f"Amount debited from account {self.acc_no} successfully! Available balance: {self.balance}")
        else:
            print("Insufficient balance")
    
    def get_account_details(self,acc_no):
        print(f"Account Number: {self.acc_no}, Balance: {self.balance}")

#transactions
Vishnu = Account(1210)
Vishnu.credit(4000)
Vishnu.debit(200)
Vishnu.credit(100)
Vishnu.debit(600)
Vishnu.debit(1000)
Vishnu.credit(5000)
Vishnu.get_account_details(1210)
Vishnu.credit(100)
Vishnu.credit(2000)
Vishnu.debit(10000)