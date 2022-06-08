
from datetime import datetime
from os import name, read
from item import Articles, Book, DigitalMedia, Items
from members import Member
from userRegister import Register
from random import randint

'''Library class is where the main functunalities such as search is implemented. A library object is created first in the main before any of them is used.'''

class Library():

    

    item_dict = dict.fromkeys(["Type", "Title"])

    def __init__(self, name = "", location = "", headLibrarian = "", capacity = "", unique_id_counter = 20):
        self.name = name
        self.unique_id_counter = 20 #numbers of item currently in the library
        self.location = location
        self.headLibrarian = headLibrarian
        self.capacity = capacity

    def __str__(self) -> str:
        return "\nThis is the library of {}, located in {}, run by head librarian: {} and has max capacity of {}. ".format(self.name,self.location,self.headLibrarian,self.capacity)
    

    '''Utility function that keeps track of new ids for member registerations, transactions and new donations'''

    def idCounter(self) -> int:
        self.unique_id_counter = self.unique_id_counter + 1
        return self.unique_id_counter

    '''Search for the item and if found, returns the item (of items class). if not, returns -1'''
    def searchItem(self):
        searchWord = input("Please enter the item title: ")
        myList = self.parseLine(searchWord) 
        '''If the return type from the parseline is a list, this means it found an item.'''
        '''Then it looks for the type of object if it is a book, digital media or Article.'''
        if type(myList) is list: 
            if myList[0] == "Book":
                myBook = Book(myList[1], myList[2])
                print(myBook)
                return myBook
            elif myList[0] == "Digital Media":
                myDigitalMedia = DigitalMedia(myList[1], myList[2])
                print(myDigitalMedia)
                return myDigitalMedia
            else:
                myArticle = Articles(myList[1], myList[2])
                print(myArticle)
                return myArticle
        else:
            print("Cannot find the item!")
            return -1

    '''Utility function that Looks if the search word exist in the items.txt,  returns list of properities if so or -1 if not.'''

    def parseLine(self, searchWord: str):
        try:
            file = open("items.txt", "r")
            read = file.readlines()
            file.close()
            for sentence in read:
                myList = list(sentence.split(","))

                '''At the end of items.txt, it will return /n which would only have one item, so'''
                '''if I don't check this, it will throw an out of bound error as myList[1] would not exist'''

                if myList[0] == "\n":
                    return -1
                if myList[1] == searchWord: #returns the list if the title is found otherwise an error code -1
                    return myList
            
            return -1
        except FileExistsError:
            print("The file is not here")

    '''Displays all the catalog by going over the items.txt. Then suggest user to select one from the menu.'''

    def displayAll(self):
        print("Here is our catalog: ")
        catalog = []
        try:
            file = open("items.txt", "r")
            read = file.readlines()
            file.close()
            for sentence in read:
                if sentence != "\n":
                    catalog.append(list(sentence.split(",")))
                
            for item in catalog:
                print(item[1], item[2])
            print("You can use the menu to reserve or return one.")

        except FileExistsError:
            print("The file is not here.")

    '''Utility function that checks if an item is in borrowing.txt already and is borrowed, returns bool'''

    def isBorrowed(self, item: Items) -> bool:
        try:
            file = open("borrowing.txt", "r")
            read = file.readlines()
            file.close()
        except FileExistsError:
            print("Cannot find the item.")
        for sentence in read:
            myList = list(sentence.split(","))
            if myList[0] == item.name:
               return True
        return False
    
    '''Writes the users book to borrowing.txt and changes it status. Also checks user has a fee.'''
    def borrow(self,item: Items, user: Member):
        
        '''Checks if the item is already reserved on borrowing.txt'''

        if self.isBorrowed(item):
            print("Unfortunately, This item is already taken.")
            return 
        

        '''checks if the user balance is less than 200, the limit to borrow a new item'''

        if user._balance < 200:
            borrowList = open('borrowing.txt', 'a')
            '''Writes to the next line the name of the item, the user and the date'''
            borrowList.write((item.name+","+ user.name+ "," + str(datetime.today())) + "\n")
            borrowList.close()
            print("The item borrowed succesfully.")
            item.changeStatus("Available")
            return

        else:
            print("Please pay your outstanding fees before trying to borrow.")
            return

    '''Allows user to return a book. If user has outstanding fees, first she needs to pay them, if not, it calls to delete function.'''

    def returning(self, item: Items, user: Member):

        if not self.isBorrowed(item):
            print("The item is not borrowed, therefore cannot be returned.")
            return 
        
        '''Calculates the fee with user input'''
        
        daysLate = int(input("How many days the book is late?"))
        fees = item.calculateFees(daysLate)
        print("Your outstanding fees from this item is: {}  ".format(fees))
        user.addFees(fees)

        '''If user balance is more than 100, she needs to pay before going forward with the transaction'''

        if  user.showBalance() > 100:
            print("You have {} outstanding fees at total. You cannot return a book without paying.".format(user.showBalance()))
            if input("Do you wanna pay right now?(Y/N) ").lower() == "y":
                user.payFees(int(input("Enter the amount you willing to pay: ")))
                if user.showBalance() < 100: 
                    print("You have sucessufly paid your fees.")
                    self.delete(item, user)
                    del(item)
                else: 
                    print("You must pay more to use this functionality. You will be returned to the main menu.")
            else:
                print("You cannot return the item without paying the fee. you will be returned to the main menu. ")
        else:
            
            self.delete(item,user)
            del(item) # end of the software objects life time, it is gonna be created again when it is searched or wanted

    '''Open the borrowing file, and writes back lines unless the items name is in that line'''

    def delete(self,item: Items, member: Member):
        with open("borrowing.txt","r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                '''checks if the item  in the line that it is about to re-write and does not re-write if it is there'''
                if item.name not in line:
                    print(line)
                    f.write(line)
            f.truncate()
        '''Lastly, sends the user a message to show the action is sucessfull'''
        print("{} is succesfully returned.".format(item.name))

        
 

    '''It writes the donation data to the items.txt'''

    def donate(self):
        type = input("Please enter the type of the item (Book, Digital Media, Article): ")
        itemName = input("Please enter the title of the item: ")
        authorName = input("Please enter the Author's Name: ")
        newId = self.idCounter()
        donationList = open('items.txt', 'a')

        '''Writes to the next line the type, name, authorname of the item in compliance with the format of items.txt'''

        donationList.write(type +","+ itemName + "," + authorName + "," + str(newId) + "\n")
        donationList.close()
        print("The book is donated succesfully. Thank you for your donation!")
           
          


        


