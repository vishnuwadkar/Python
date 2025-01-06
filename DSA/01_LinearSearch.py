#locate a card in a deck of sorted cards in descending order 
def locateCard(cards, target):      #cards is the list of cards and target is the element to be found
    #this function will return the position of the target card
    pass

myCards = [19,15,13,9,7,4,3,2]
target = 7
output = 4

#test case as a dictionary
test = {
    'input':{
        'myCards':  [19,15,13,9,7,4,3,2],
        'target': 7
    },
    'output': 4
}

#locateCard(**test['input']) == test['output']    ** uses the values of keys as arguments

#solving by linear search algorithm
def locateCard(cards, target): 
    position = 0    # counter for position
    n = 1 # counter for the number of cards
    for card in cards:  # loop through the list of cards
        if card == target:  # if the card is found
            return position, n  # return the position of the card
        else:
            position += 1  # increment the position counter if the card is not found
            n += 1  # increment the counter for the number of cards
    else:
        return -1  # return -1 if the card is not found in the list

print(f"The card is at position: {locateCard(myCards,target)[0]} in {locateCard(myCards,target)[1]} card flips")


yourCards = []  #an empty array
print(f"The card is at position: {locateCard(yourCards,target)}")

#the TIME COMPLEXITY of linear search algorithm is O(n) where n is the number of elements in the list
#the SPACE COMPLEXITY of linear search algorithm is O(1) as it uses a constant