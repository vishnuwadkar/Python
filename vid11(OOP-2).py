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
#function used as an attribute / property

class myName:

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):  #this name function is used as an attribute and not as function
        self.fname, self.lname = value.split()

obj = myName()
obj.name = "John Doe"
print(obj.name)  #John Doe
print(obj.fname)
print(obj.lname)

#this is abstraction and encapsulation
#encapsulation is hiding the data and abstraction is hiding the implementation details


#OPERATOR OVERLOADING
class Number:
    def __init__(self, n):
        self.n = n
    def __add__(self,num):
        return self.n + num.n  #doesn't gives error now

n = Number(1)
m = Number(3)
print(m+n)      #usually not possible, gives error for +

'''
Operator methods:
p1.__sub__(p2)
p1.__mul__(p2)
p1.__truediv__(p2)
p1.__floordiv__(p2)
'''

#str__() ->used to set what gets displayed upon calling str(obj)

#these are all dunder methods

#Q. Create a class vector representing n dimensions. Overload the + and * operators to add two vectors and dot profuct of them
class Vector:
    def __init__(self, x, y ,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        return result
    
    def __str__(self):
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"

v1 = Vector(2,3,4)
v2 = Vector(21,7,14)
v3 = Vector(9,30,41)

print(v1+v2)    #Vector(23, 10, 18)
print(v1*v3)    #Vector(18, 90, 164)

print(v1+v3)    #Vector(11, 33, 45)
print(v2*v3)    #Vector(189, 210, 574)