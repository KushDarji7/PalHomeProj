
class Tenet:
    
        #creates a new Tenet variable with attributes guestof_name, room number and rate
        #tenet constructor
        # add addtional notes of variables to add that are not requried
            # like guest info, maintence stuff, 
            # integrate room cleaning check
            # appliences
            # key reset
            # balances 
            
    def __init__(self, guest_name, room, rate):
        self.guest = guest_name
        self.room = room
        self.rate = rate
    
    def retrive_tenet(self):
        return print("\nTenet:", self.guest_name, "\nRoom #:", self.room, "\nRate:", self.rate)
        
