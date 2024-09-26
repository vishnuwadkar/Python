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







