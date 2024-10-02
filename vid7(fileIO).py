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
    myfile.write("Hi Everyone\nwe are learning file I/O\nusing java.\nI like programming in Java.")
    


