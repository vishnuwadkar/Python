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

