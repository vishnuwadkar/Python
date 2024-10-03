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
