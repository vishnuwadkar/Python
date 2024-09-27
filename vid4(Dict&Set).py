#DICTIONARIES AND SETS IN PYTHON

'''Dictionaries are used to store data in 'key:value' pairs
    They are unordered,  mutable, and can be used to store any type of data'''
# Creating a dictionary
dict = {
    "name": "Vishnu",
    "age": 20,
    "city": "Pune",
    "student": True,
    "marks": [90, 80, 70],  #lists and tuples can also be used  as values
    "subject"  : ("English","Math","Science")   #tuples can be used as key as well
}
#values are accessed using  keys and not indexes
print(dict["name"])
print(dict["age"])
print(dict["city"])
print(type(dict))
#assigning value
dict["age"]=21
print(dict["age"])
print(dict)

null_dict = {}  #an empty dictionary 

#NESTED DICTIONARIES
#A dictionary can have another dictionary as its value
nested_dict = {
    "name":"Vishnu",
    "roll_no":52,
    "marks":{   #dict inside a dictionary
        "phy":97,
        "chem":98,
        "math":99
    }
}

#accessing nested dict
print(nested_dict["marks"]["phy"])
print(nested_dict["marks"]["chem"])
print(nested_dict["marks"]["math"])

#dictionary methods
#1.  keys() = returns all keys from the dictionary
print(dict.keys())
print(list(dict.keys()))    #typecasting to list

#2. values() = returns all the values from the dict
print(dict.values())
print(list(dict.values()))    #typecasting to list

#3. items() = returns all key:value pairs as tuples
print(dict.items())
print(list(dict.items()))    #typecasting to list

pairs = list(dict.items())
print(pairs[1])

#4. get("key") = returns value at key
print(dict.get("name")) #returns None of key not present

#5.update(newDict) = inserts the specified items to dictionary
dict.update({"city":"Mumbai"})  #city updated
print(dict)

new_dict = {
    "marks":89,
}
dict.update(new_dict)   #this is acceptable as well

#6. pop("key") = removes the specified key-value pair from dictionary
dict.pop("city")
print(dict)

#Note: get methods returns None while normal accessing by key produces error if  key is not present
#       an error in code exec doesn't allow further code exec!

#SETS IN PYTHON

#Set is a collection of the unordered items. Each element in the set must be unique and immutable
#tuple can be stored in a set, but not a dictionary and list since they are mutable

collection = {1,2,2,3,4}
print(collection)   #duplicate values are ignored
print(type(collection))
print(len(collection))   #duplicates exclude

#emtpy set syntax
e_set = set()   #since {} is syntax for empty dictionary 

#methods of set

# 1.add("value") -> adding elementto set
collection.add("Hi")
collection.add("Hi")
print(collection)   #duplicate values are ignored

#2. remove(val) -> remove values from set
collection.remove("Hi")
print(collection)  

#Unhashable i> mutable 

#3. clear() -> empties the set

#4. pop() -> removes a random value from set
'''print(collection.pop())
print(collection.pop())
print(collection)  '''

# .union(set) -> cobines two sets and returns new
u_set = {10, 90,"diya",2,3}
set2 = collection.union(u_set)
print(set2)

# .intersection(set) -> returns a set of common elements
set2 = collection.intersection(u_set)
print(set2) #2 and 3 common

#Q. Store the following word meanings in a python dictionary

words = {
    "cat":"a small animal",
    "table": ["a piece of furniture","list of facts and figures" ]
}
print(words)

''' Q. We are given a list of subjects for students. Assume one classroom is 
    reqd for 1 subject, How many classroom are required  by all student'''

subjects = {"Python", "java", "Cpp", "Python", "Javascript", "java", "Python", "java", "Cpp","C"}   #set of classroom
print("No of classroom reqd would be: ", len(subjects)) #prints 5

'''Q. Write a program to enter marks of 3 subjects from the user and store the in a dictionary.
    Start with an empty and add one by one. USe subject name as key and marks as value'''

marks = {}

eng = int(input("Enter English marks: "))
math = int(input("Enter math marks: "))
history = int(input("Enter history marks: "))

marks.update({"english":eng})
marks.update({"math":math})
marks.update({"history":history})

print(marks)

#Q. Figure out a way to store 9 & 9.0 as separate values in set using built in datatypes

values = {
    ("int",9),      #tuples
    ("float",9.0)
}
print(values)
#another way is to store one of the either as a string








