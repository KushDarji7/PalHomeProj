

#imports 

class Tenet:
    
    #creates a new variable with attributes of guest name, room number and price
    #tenet constructor
    def __init__(self, room, guest, price, note):
        self.room = room
        self.guest = guest
        self.price = price
        self.note = note
    
    def retrieve_tenet(self):
        print("\ntenet:", self.guest, "\nroom:", self.room, "\nprice: $", self.price)
        
    def addTenet(self):
        print("adding Tenet's \n please wait ... ")
        
    def showMeTenet(self):
        print("showing Tenet's \n please wait ... ")
        return self.room
        
    
#using johnson trotter algo to make permutation of all room number
#1-16, -1... b/c there is no 13, 
#occupied and vaccant statush

# print("foo")
R103 = Tenet('103', "Joe Cruz", 290, "this is the OG him self, cuban \'mafia\' man")
R103.retrieve_tenet()

# print("bar")
R105 = Tenet('105', "STORAGE", 'null', "NO CHANGE, utility room")
R105.retrieve_tenet()
        
        
