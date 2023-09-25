

#imports 

class Tenet:
    
    #creates a new variable with attributes of guest name, room number and price
    #tenet constructor
    def __init__(self, guest, room, price):
        self.guest = guest
        self.room = room
        self.price = price
    
    def retrive_tenet(self):
        print("\ntenet:", self.guest, "\nroom:", self.room, "\nprice:", self.price)
        
    
#using johnson trotter algo to make permutation of all room number
#1-16, -1... b/c there is no 13, 
#occupied and vaccant status

# print("foo")
R103 = Tenet('Joe', "103", 95)
R103.retrive_tenet()

# print("bar")
R105 = Tenet('STORAGE', "105", 'null')
R105.retrive_tenet()
        
        
