
class Room:
    def __init__(self, room_num, capacity, is_booked= False, is_weekly=False, is_roomService=False):
        self.room_num = room_num
        self.capacity = capacity
        self.is_booked = is_booked
        self.is_weekly = is_weekly
        self.is_roomService = is_roomService

class Hotel:
    def __init__(self, name, num_rooms):
        self.name = name
        self.rooms = [Room(room_num, capacity) for room_num, capacity in enumerate(range(1, num_rooms +1 ), start = 1 )]

    def display_available_rooms(self):
        available_rooms = [room for room in self.rooms if not room.is_booked]

        if available_rooms:
            print("available Rooms: ")
            for room in available_rooms:
                print(f"Room Number: {room.room_num}, Capacity: {room.capacity}, Vacant: {room.is_booked}")
        else:
            print("\n   No rooms available!")
    
    def book_room(self, room_num):
        room = self.rooms[room_num - 1]

        if not room.is_booked:
            room.is_booked = True
            print(f"Room {room_num} : booked Successfully.")
        else:
            print(f"\n  Room {room_num} is already booked.")
        
        return room
        
    def checkout_room(self, room_num):
        room = self.rooms[room_num - 1]
        if room.is_booked:
            room.is_booked = False
            print(f"Room {room_num} checked out successfully.")
        else:
            print(f"Room {room_num} is not booked.")


def main():
    hotel = Hotel("Gwinnett Inn", 14)
    while True:
        print("\nHotel Management System")
        print("1. Display Available Rooms")
        print("2. Book a Room")
        print("3. checkout of a Room")
        print("4. Exit")

        choice = input("Enter your choice:")
        if choice == "1":
            hotel.display_available_rooms()
        elif choice == "2":
            room_num = int(input("enter room number to book: "))
            if 1 <= room_num <= len(hotel.rooms):
                hotel.book_room(room_num)
            else:
                print("Invalid room number.")
        elif choice == "3":
            room_num = int (input("Enter room number to check out: "))
            if 1 <= room_num <= len(hotel.rooms):
                hotel.checkout_room(room_num)
            else:
                print("Invalid room number.")
        elif choice == "4":
            print("Thank you for using the HMS. \n GOODBYE!")
            break
        else:
            print("invalid choice.\n PLEASE ENTER VALID OPTION.")
if __name__ == "__main__":
    main()
            
