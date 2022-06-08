from datetime import date

class Items:
    
    def __init__(self, name = "", type = "", id = 0, author = "", status = "Available"):
        self.name = name
        self.type = type
        self.id = id
        self.author = author
        self.status = status

    def __str__(self) -> str:
        return "This is an item class"

    def changeStatus(self, status: str) -> None:
        self.status = status
    def calculateFees(self, fees: int, daysLate: int) -> int:
        return fees * daysLate
    
class Book(Items):

    def __init__(self, name = "", author = "", type = "", id = 0, status = "Available", edition = "", publisher = "", page = 0, fees = 50): 
        Items.__init__(self, name, type, id, status)  
        self.author = author
        self.edition = edition
        self.publisher = publisher
        self.page = page
        self.fees = fees

    def __str__(self) -> str: 
        return "\nThe book name is {}, written by {} and {} for borrow.\n".format(self.name, self.author, self.status)

    '''returns the calculated fees for the book by overriding the parent method'''
    def calculateFees(self, daysLate: int) -> int: 
        return self.fees * daysLate
    
class DigitalMedia(Items):
    def __init__(self, name = "", author = "", type = "", format = "",id = 0, edition = "", status = "Available", publisher = "", page = 0, fees = 20):
        Items.__init__(self,name, type, id, status)  
        self.author = author
        self.format = format
        self.page = page
        self.edition = edition
        self.publisher = publisher
        self.fees = fees
       
    def __str__(self) -> str: 
        return " \nThe Digital Media's name is {}, written by {} and {} for borrow.\n".format(self.name, self.author, self.status)  
    
    def calculateFees(self, daysLate: int) -> int: 
        return self.fees * daysLate
    
    
class Articles(Items):
    def __init__(self, name = "", author = "", type = "", format = "", id = 0, status = "Available", volume = "", journal = "", fees = 30):
        Items.__init__(self,name, type, id, status)  
        self.author = author
        self.journal = journal
        self.volume = volume
        self.format = format
        self.fees = fees
        
    def __str__(self) -> str: 
        return "\nThe Article name is {}, written by {} and {} for borrow.\n".format(self.name, self.author, self.status)  
    
    def calculateFees(self, daysLate: int) -> int: 
        return self.fees * daysLate
       




