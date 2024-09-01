class Movie:
    time=0
    language=""
    animations=""
    genre=""
    
    def __init__(self,time,language,animations,genre):
        print("Hello")
        self.time=time
        self.language=language
        self.animations=animations
        self.genre=genre
    
    def getValue(self):
        self.time=int(input("Enter how long the movie is (in hours):"))
        self.language=input("Enter the language: ")
        self.animations=input("Do you want the movie to be animated? ")
        self.genre=input("Enter the movie genre: ")

    def displayOutput(self):
        print("The movie is",self.time,"hours long")
        print("This book is written in "+self.language)
        print("Your choice for animations is "+self.animations)
        print("The movie genre is "+self.genre)

movie1=Movie(2,"Spanish","Yes","Mystery")
movie2=Movie(1.5,"English","No","Horror")
movie1.getValue()
movie1.displayOutput()
movie2.displayOutput()