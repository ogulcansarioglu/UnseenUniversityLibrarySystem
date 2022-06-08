import re


class Register():

    def __str__(self) -> str:
        return "The register class that has the user registration utility functions"

    '''Looks up if the user name is already in the file, if so, returns true, false otherwise'''
    def isRegistered(memberName: str) -> bool:
        try:
            file = open("members.txt", "r")
            read = file.readlines()
            file.close()
            for sentence in read:
                myList = list(sentence.split(","))

                if str(myList[0]) == memberName: 
                    return True
            return False
        except FileExistsError:
            print("The file is not here")
    
    '''Handles user registeration'''
    def userRegister(userId: int) -> bool:
            '''Checks if the user is already registered and returns if so'''
            
            memberName = input("Please enter your username: ")
            password = input("Please enter your password: ")

            if Register.isRegistered(memberName):
                print("The username already exists! ")
                return False
            elif Register.passwordValidation(password) == False:
                print("The password is invalid. It must include a number, a lower and an uppercase, a unique char and 6-30 characters")
                return False
        
            '''If not, it adds user information to the end of the members file'''
            try:
                memberList = open('members.txt', 'a')
                memberList.write(memberName + "," + password + "," + str(userId) + '\n')
                memberList.close()
                print("addded!")
                return True
            except FileExistsError:
                return False
            
          

    '''Usage of regex, clean and a smart solution that I learned from https://www.geeksforgeeks.org/password-validation-in-python/'''
    def passwordValidation(password: str) -> bool:
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,30}$"
      
        '''compiles the regex'''
        validPattern = re.compile(reg)
      
        '''searches the regex and stores and returns the bool value in mat'''               
        mat = re.search(validPattern, password)
        return True if mat else False

        
    def authorize(self,membername: str, password: str) -> bool:
        if self.isRegistered(membername):
            return True
        else:
            return False
    

