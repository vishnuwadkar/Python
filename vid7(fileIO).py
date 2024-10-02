#FILE I/O IN PYTHON
#=====================================
#Python can be used to perform operations on a file (read and write data)
#Types of files: Text files and Binary files

#READ MODE
'''f = open("demo.txt","r")  #if file is not in parent directory , you need to specify the path
data = f.read()     #f is a variable given to the file, read() function stores all the data to 'data' variable
print(data)
print(type(data))

data2 = f.readline()
print(data2)
data3 = f.readline()
print(data3)
#data once read earlier, is not read again since pointer/cursor is shifted at last
f.close()   #closing a file  is good practice to avoid memory leak
'''

#WRITE MODE
f = open("demo.txt","w")    #w - write mode overwrites to the file i.e previous data is truncated
f.write("Hello, Python!")
f.close()

f = open("demo.txt","a")    #append mode is used to add to the file i.e append
f.write("\nThis is a Python tutorial!")
f.close()

#When file is opened for writing or appending, if the  file does not exist, it is created!

#THE with SYNTAX:

with open("demo.txt","r") as x:     #automatically closes the files after the code block
    data = x.read()
    print(data)

with open("demo.txt","w") as y:
    y.write("This is writing in a file")    #overwrites this line to the file

with open("demo.txt","r") as x:     #automatically closes the files after the code block
    data = x.read()
    print(data)

#DELETING A FILE
#we have to use 'os module'  to delete a file
import os
os.remove("demo.txt")
#file is deleted now!

#Q. Create a file 'practice.txt' and add the following to it:

with open("practice.txt","w") as myfile:
    myfile.write("Hi Everyone\nwe are learning file I/O\nusing Java.\nI like programming in Java.")

#Write a function to replace Java with Python
with open("practice.txt","r") as myfile:
    data = myfile.read()

newdata=data.replace("Java","Python")
print(newdata)
with open("practice.txt","w") as myfile:
    myfile.write(newdata)

#Search if 'learning' exist in the file or not
def checkword(word):    #function that takes word as argument
    with open("practice.txt","r") as myfile:
        data = myfile.read()
        if data.find(word) != -1:
            print("Found in the file")
        else:
            print("Not found in the file")

checkword("learning")   #function call

#Write a function that checks for word and tell the line in which it is present, print -1 if not present
def checkLines(word,filename):
    data = True
    line=1
    with open(filename,"r") as myfile:
        while data:
            data = myfile.readline()
            if word in data:
                print("Present in line number ",line)
                return
            else:
                line += 1
        else:
            print(-1)
            return

checkLines("learning","practice.txt")  #prints line 2
checkLines("programming","practice.txt")  #prints line 4
checkLines("xprogramming","practice.txt")  #prints line 4

#Q.From a file separated by commas, print how many number are even 
with open("prac2.txt","r") as f:
    data = f.read()
    print(data)
    
    nums = data.split(",")  #creating a list named nums splitted by ','
    print(nums)
    count = 0
    for ele in nums:
        if int(ele)%2==0:   #even number check
            count+=1        #if even, increase count
    else:
        print(f"There are {count} even numbers")  #prints the  count of even numbers


'''
To print all numbers from a file without using split
    num=""
    for i in range(len(data)):
        if data[i]==",":
            print(int(num))
            num=""
        else:
            num += data[i]
    else:
        print(int(num))'''
    
os.remove("prac2.txt")
os.remove("practice.txt")

