from math import trunc
from Library import Library 
from members import Member
from item import Items
from userRegister import Register

"User interface where user interacts with the system using the menu"

class userInterface:

    def __str__(self) -> str:
        return "The user interface class."
    
    def showMenu(self, myLibrary: Library):
        try:
            '''press-key dictinory to show the user which functunality each key activates'''
            press_key_list = {"S" : "Search Item", "D": "Display All Items", "B": "Borrow Item", "A": "Donate Item", "R": "Return Item", "P": "Check Balance and Pay" , "Q": "Quit"}

            key_press = False
            
            '''Bool for if the user logged in in the system'''
            registered = False

            '''If user does not press quit or an error occurs, keep showing the login/register and then, menu'''
                
            while not (key_press == "q"):
                print("\n______________ Welcome to {} Management System______________ \n".format("Unseen University"))

                '''First, ask user to login or register until they do'''

                while not registered:
                    keyInput = input("Login or Register(L/R) ").lower()
                    if keyInput == "l":
                        userName = input("Please enter your username: ")
                        password = input("Please enter your password: ")

                        registered = Register.isRegistered(userName)
                        if registered == False:
                            print("Username or password is wrong")
                    elif keyInput == "r":
                        print("\n You can register here.\n")
                        if Register.userRegister(myLibrary.idCounter()):
                            print("\n Now you can login with your credentials.\n")
                        else:
                            print("Try again!")
                            
                '''creates the user by calling member class with username and password'''
                currentUser = Member(userName, myLibrary.idCounter(), password)
    
                print("\nHello, {}, please see your options: \n".format(currentUser.name))
                        
                for key, value in press_key_list.items():
                    print("Press", key, "to", value)
                key_press = input("Press Key: ").lower()

                '''Menu Functions'''

                if key_press == "b":
                    print("\nCurrent Selection: Borrow Item \n")
                    reservedItem = myLibrary.searchItem()
                    if reservedItem != -1:
                        myLibrary.borrow(reservedItem, currentUser)

             
                
                elif key_press == "s":
                    print("\nCurrent Selection: Search Item \n")
                    searchItem = myLibrary.searchItem()
                    if searchItem != -1:
                                
                        userInput = input("Do You Want to Borrow This Item?(Y/N) ").lower() #User would not just want to search the book, but borrow it if it is found so I added here
                        if userInput == "y":
                            myLibrary.borrow(searchItem, currentUser)
                        else:
                            print("You will be returned to the main menu")
                            
                elif key_press == "a":
                    print("\nCurrent Selection: Donate Item \n")
                    myLibrary.donate()
                           
                elif key_press == "p":
                    print("Current Selection: Check Balance and Pay\n")
                    print("Your balance is: {}".format(currentUser.showBalance()))
                    payment = input("Please provide the amount you want to pay: ")
                    currentUser.payFees(int(payment))
                    print("Your balance is: {}".format(currentUser.showBalance()))
                        
                elif key_press == "d":
                    print("\nCurrent Selection: Display Item \n")
                    myLibrary.displayAll()
                            
                elif key_press == "r":
                    print("\nCurrent Selection: Return Item \n")
                           
                    reservedItem = myLibrary.searchItem()
                    if reservedItem != -1:
                        myLibrary.returning(reservedItem, currentUser)

                            
                elif key_press == "q":
                    break
                else:
                    continue
        except Exception as e:
                print("Something went wrong :( Please check your input.")

