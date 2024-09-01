class Book:
    pages=0
    language=""
    illustrations=""
    author=""
    price=0.0

    #Constructor
    def __init__(self,pages,language,illustrations,author,price):
        print("Hello")
        self.pages=pages
        self.language=language
        self.illustrations=illustrations
        self.author=author
        self.price=price
    
    #Getting values from the user 
    def getValue(self):
        self.pages=int(input("Enter the number of pages:"))
        self.language=input("Enter the language: ")
        self.illustrations=input("Do you want illustrations? ")
        self.author=input("Enter the author's name: ")
        self.price=int(input("Enter the price:"))

    def displayOutput(self):
        print("The number of pages in this book is",self.pages)
        print("This book is written in "+self.language)
        print("Your choice for illustrations is "+self.illustrations)
        print("The author's name is "+self.author)
        print("The price of the book is",self.price)

book1=Book(300,"English","No","Lauren Roberts",8)
book2=Book(250,"French","No","Holly Jackson",10)

book1.getValue()
book1.displayOutput()

book2.displayOutput()