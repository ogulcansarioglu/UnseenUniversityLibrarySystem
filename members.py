'''Member class stores protected user information and using get, set functions adjust or show the balance'''

class Member:
    def __init__(self, name = "", id = 0, _password = "", _balance = 0) -> None:
        self.name = name
        self._password = _password
        self._balance = _balance
        self.id = id
        
    def __str__(self) -> str:
        return "The user's name is ".format(self.name) 

    '''Gets the balance of user, as it is protected.'''

    def showBalance(self) -> int: 
        return self._balance
    
    '''Add fees to the balance'''

    def addFees(self, fees: int) -> None:
        self._balance = self._balance + fees

    '''Decrease the payment from the balance and let the user know'''

    def payFees(self, payment: int) -> int:
        self._balance = self._balance - payment
    
    def feesPaid(self) -> bool:
        if self._balance <= 0:
            return True
        

    
    

        
        
    


