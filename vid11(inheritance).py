#-----INHERITANCE------
# syntax for Inheritance-> class ChildClass(ParentClass):

class Employee:
    company = "Google"

    def __init__(self, salary, languages):
        self.salary = salary
        self.languages = languages
    
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary} and the company is {self.company}")

    
class Programmer(Employee):     #programmer inherited from Employee
    def __init__(self, name, salary, languages):
        self.name = name
        self.salary = salary
        self.languages = languages
    
guy = Programmer("Rahul", 10000, ["Python", "Java"])
guy.showDetails()   #function of employee class for object of programmer class

#Multiple inheritance 
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Name is {self.name} and age is {self.age}")

class Developer(person, Employee):
    def __init__(self, name, age, salary, languages):
        person.__init__(self, name, age)
        Employee.__init__(self, salary, languages)

    def show(self):
        print("Developer details")
        print(f"Name is {self.name} and age is {self.age} and salary is     {self.salary} and languages are {self.languages}")
    
    

myDev = Developer("Harry",32,230002,"Python")
myDev.show()  #calling the show method of Developer class which is calling the show method of


#MULTILEVEL INHERITANCE

class A:
    a=1

class B(A):
    b=2

class C(B):
    c=3

#C is the child of B and B is the child of A
#C is the grandchild of A
#C is the child of A through B

o = A()
print(o.a)  #1

p = B()
print(p.a,p.b)  #1  #2

q = C()
print(q.a,q.b,q.c)  #1 2 3

#SUPER keyword

class A:
    a=1
    def __init__(self):
        print("A class constructor")

class B(A):
    b=2
    def __init__(self):
        print("B class constructor")

class C(B):
    
    c=3
    def __init__(self):
        super().__init__()      #runs B class constructor before C
        #Thus super is parent class
        print("C class constructor")

'''o = A()
print(o.a)  #1

p = B()
print(p.a,p.b)  #1  #2'''

q = C()
print(q.a,q.b,q.c)  #1 2 3
#runs constructor of C only, and not A and B

#CLASS METHODS
#directly accessing a method of a class
#without creating an object of the class

class A:
    a = 1
    @classmethod
    def class_method(cls):
        print(f"The class attribute is {cls.a}")  #prints 1

a = A()
a.a = 3
a.class_method()    #this prints 1, but wouldve printed 3 if it was an instance method

#PROPERTY DECORATORS
#used to create a property of a class
