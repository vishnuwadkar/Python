#LOOPS IN PYTHON

#loops are used to repeat instructions s

# WHILE LOOP:

i=1     #iterator
while i<6:  #condn
    print("Hello")  #statement
    i+=1    #increment
print("Loop ended")

# printing numbers from 1 to 10
i=1
while i<=10:
    print(i)
    i+=1
print("Done")

#print numbers from 1 to 100
'''i=1
while i<=100:
    print(i)
    i+=1
print("Done")'''

#print numbers from 100 to 1
'''i=100
while i>=1:
    print(i)
    i-=1
print("Done")'''

#print multiplication table of number n
'''n=5
i=1
while i<=10:
    print(n*i)
    i+=1'''

# print elements of the following list using loop
list = [23,45,22,19,9,56,54,33,91,100]
i=0
while i<(len(list)):
    print(list[i])
    i+=1

#search for number x in the following tuple
tup = (23,78,22,28,91,78,75,10,4,34)
x = 10
i=0
while i<len(tup):
    print("finding...")
    if tup[i]==x:
        print("Element found in the list at ",i,"!")
        break
    else:
        i+=1

#break keyword is used to terminate the loop when encountered
#continue keyword terminates execution in the current iteration & continues execution of the loop with next iteration
i=0
while i<5:
    if(i==3):
        i+=1
        continue    #3 will be skipped
    print(i)
    i+=1
print("done")

#FOR LOOPS
#used for sequential traversal in list, string, tuples

lst = [1,2,3]       #traversing a list without indexes
for element in lst:     #in is a keyword
    print(element)  #printing all elements 
print("done")

tup = (23,43,100,35)
for nums in tup:
    print(nums)
print("done")

# for loop with else: does work after terminating the loop
tup = (23,43,100,35)
for nums in tup:
    print(nums)
else:       #needs where break is used
    print("done")   #only executes if the loop is completely executed

#search for number x in the following tuple
tup = (23,78,22,28,91,78,75,10,4,34)
x=7
i=0
for el in tup:
    if(el==x):
        print("Found at index ",i)
        break
    i+=1
else:
    print("Number not found")

#RANGE: range function returns a sequence of numbers, starting from 0 by default, 
#       and increments by 1(default), and stops before a specified number

# Syntax: range(start?,stop,step?)

for el in range(5): #range(stop)
    print(el)   #prints 0 to 4
    
for el in range(20,30):     #range(start,stop)
    print(el)   #prints 20 to 29

for el in range(0,100,10):  #range(start,stop,step)
    print(el)   #prints with a step of 10
    
#print numbers from 100 to 1 using range
for el in range(100,0,-1):
    print(el)

#print multiplication table of n
n=5
for i in range(1,11):
    print(n*i)

#PASS STATEMENT
#pass is null statement that does nothing. It is used as a placeholder for future code

for el in range(10):
    pass    #does nothing
#mostly used in try-catch

#Write a program to find sum of first n numbers
n = int(input("Enter number: "))
i=0
sum = 0
while i<=n:
    sum += i
    i+=1
print(sum)

#factorial of a number using loops
n = int(input("Enter number: "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print("factorial: ",fact)