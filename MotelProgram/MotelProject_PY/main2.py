class Hotel:
    def __init__(self):

        self.rooms = {
            101: {"type": "Single", "price": 95, "booked": False, "guest": None},
            102: {"type": "Single", "price": 95, "booked": False, "guest": None},
            103: {"type": "Single", "price": 95, "booked": False, "guest": None},
            104: {"type": "Single", "price": 95, "booked": False, "guest": None},
            201: {"type": "Single", "price": 95, "booked": False, "guest": None},
            202: {"type": "Single", "price": 95, "booked": False, "guest": None},
            203: {"type": "Single", "price": 95, "booked": False, "guest": None},
            204: {"type": "Single", "price": 95, "booked": False, "guest": None},
        }

    def view_available_rooms(self):
        print("\n Available Rooms:")
        for room_num, details in self.rooms.items():
            if not details["booked"]:
                print(
                    f"Room {room_num}: {details['type']} - ${details['price']} per night"
                )

    def book_room(self):
        self.view_available_rooms()

        try:

            room_num = int(input("\nEnter the room number you want to book: "))

            if room_num in self.rooms and not self.rooms[room_num]["booked"]:
                guest_name = input("Enter your name: ")
                self.rooms[room_num]["booked"] = True
                self.rooms[room_num]["guest"] = guest_name
                print(f"\nRoom {room_num} SUCCESSFULLY booked for {guest_name}.")
            else:
                print("\nRoom is either not available or occupied.")
        except ValueError:
            print("\nInvalid input.\nPLease enter a valid room number.")

    def check_booking(self):
        guest_name = input("\nEnter guest name to check booking: ")
        found = False
        for room_num, details in self.rooms.items():
            if not details["booked"] and details["guest"] == guest_name:
                print(
                    f"\n{guest_name} has booked Room {room_num}: {details['type']} - ${details['price']} per night."
                )
                found = True
                break
        if not found:
            print("\nNo booking found for this guest.")

    def check_out(self):
        guest_name = input("\nEnter guest name to check out: ")

        for room_num, details in self.rooms.items():

            if details["booked"] and details["guest"] == guest_name:
                self.rooms[room_num]["booked"] = False
                self.rooms[room_num]["guest"] = None
                print(f"\n{guest_name} has SUCCESSFULLY CHECKED OUT of {room_num}. ")
                return
        print("\nNo booking found for this guest.")

    def run(self):
        while True:
            print("\n ~~~ HOTEL BOOKING SYSTEM ~~~")
            print("1. Display Available Rooms")
            print("2. Book a Room")
            print("3. Check Booking")
            print("4. Check out ")
            print("5. Exit")

            try:

                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    self.view_available_rooms()
                elif choice == 2:
                    self.book_room()
                elif choice == 3:
                    self.check_booking()
                elif choice == 4:
                    self.check_out()
                elif choice == 5:
                    print(
                        "Thank you for using \nHotel Management System.\n Until next Time!"
                    )
                    break
                else:
                    print("\n Invalid choice. Please select a valid option.")
            except ValueError:
                print("\nInvalid input. \nPlease enter a number between 1 & 5.")


if __name__ == "__main__":
    hotel = Hotel()

    hotel.run()
