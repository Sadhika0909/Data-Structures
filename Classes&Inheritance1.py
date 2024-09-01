class HotelRoom:
    price=0.0
    size=""
    room=0
    people=0

    #constructor
    def __init__(self,price,size,room,people):
        self.price=price
        self.size=size
        self.room=room
        self.people=people
        
    
    def get_values(self):
        self.price=int(input("What is the price of the room? "))
        self.size=input("What size is your room? ")
        self.room=int(input("What is your room number? "))
        self.people=int(input("How many people are going to be staying? "))

    def displayOrders(self):
        return f"{self.price},{self.size},{self.room},{self.people}"
    
class Economy(HotelRoom):
    service=""

    def __init__(self,service,price,size,room,people):
        super().__init__(service,price,size,room,people)
    
    def display_output(self):
        return f"{self.service},{self.price},{self.size},{self.room},{self.people}"
    

