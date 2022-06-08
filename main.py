
from Library import Library
from userRegister import Register
from userInterface import userInterface

'''This is the main function that the programs runs the userinterface with and shows the menu that starts the user interaction.'''

if __name__ == "__main__":

    '''Gets the library information from the library.txt before creating a library object'''

    try:
        file = open("Library.txt", "r")
        read = file.readlines()
        file.close()
        for sentence in read:
            libraryInfo = list(sentence.split(",")) #reads from the text file into a list
    except FileExistsError:
        print("The file is not here")

    '''using list comprehension, puts the information into right variables'''

    libraryName, libraryLocation, headLibrarian, maxCapacity = [libraryInfo[i] for i in range(len(libraryInfo))]

    '''Creates the userInterface object menu and Library, starts the menu'''
    
    menu = userInterface()
    unseenLibrary = Library(libraryName, libraryLocation, headLibrarian, maxCapacity)
    print(unseenLibrary)
    menu.showMenu(unseenLibrary)


