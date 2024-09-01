class Foods:
    price=0.0
    quantity=""
    number=0
    order=0
    Type=""
    name=""

    #constructor
    def __init__(self,name,price,quantity,number,order,Type):
        self.price=price
        self.quantity=quantity
        self.number=number
        self.order=order
        self.Type=Type
        self.name=name
    
    def get_values(self):
        self.price=int(input("What is the price of the food? "))
        self.quantity=input("What size is your food? ")
        self.number=int(input("How many of this food do you want? "))
        self.order=int(input("What is the average number of order?"))
        self.Type=input("How do you want your food to be (spicy,sweet,etc.) ")
        self.name=input("Name of food: ")

    def displayOrders(self):
        return {"name":self.name,"price":self.price,"quantity":self.quantity,"number":self.number,"order":self.order,"type":self.Type}
    
class Italian(Foods):
    name=""

    def __init__(self,name,price,quantity,number,Type):
        super().__init__(name,price,"small",3,Type)
    
    def display_output(self):
        return {"name":self.name,"price":self.price,"quantity":self.quantity,"number":self.number,"type":self.Type}
    
class Indian(Foods):
    name=""
    category=""
    region=""
    veg=""

    def __init__(self,name,category,region,veg,quantity,Type):
        super().__init__(name,category,region,veg,quantity,Type)

    def display(self):
        return {"name":self.name,"category":self.category,"region":self.region,"veg":self.veg,"quantity":self.quantity,"type":self.Type}

#object creation
italian1=Italian("pizza",10,"small",2,"spicy")
indian1=Indian("panipuri","snack","north indian","Yes",2,"spicy")

print(italian1.display_output())
print(indian1.display_output())



