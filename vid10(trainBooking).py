from random import randint

class Train:
    def __init__(self, trainNo):        #takes a number (train num) as argument 
        print("Hello! Welcome to the train booking system!")
        self.trainNo = trainNo  #sets the argument as train number 
        
    def book(self, fro, to):
        print(f"Ticket is booked for train: {self.trainNo} from {fro} to {to}")
        
    def getStatus(self):
        print(f"Train: {self.trainNo} is running on time")
    
    def getFare(self, fro, to):
        print(f"The fare for train: {self.trainNo} from {fro} to {to} is {randint(300,3000)}")

t = Train(12105)
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFare("Delhi", "Mumbai")