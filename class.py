class BankAccount:
      """
                      ATTRIBUTES
      """
      # DEFAULT INITIALISATION 
      def __init__(self): 
            self.account_number = 0
            self.ssn = 123456789
            self.name = "custumer"
            self.balance = 0.00
            self.min_balance = 100.00
            self.active = False
      # PERSONALIZED INITIALISATION
      def __init__(self, acct, ss, name, balance):
            self.account_number = acct
            self.ssn = ss
            self.name = name
            self.balance = balance
            self.min_balance = 100.00
            self.active = False
      #INITIALISATION WITH PRIVATE ATTRIBUTES
      def __init__(self, number, ssn, name, surname, balance):
            self.__account_number = number
            self.__ssn = ssn
            self.__name = name
            self.__surname = surname
            self.__balance = balance
            self.__min_balance = 99
            self.__active = True
            """
                      METHODES
            """
      def deposti (self, amount):
            if self.isActive():
                  self.__balance += amount
                  return True
            return False
      
      def withdraw (self, amount):
            result = False;
            if self.isActive() and (self.__balance - amount >= self.__min_balance):
                  self.__balance -= amount;
                  result = True;
            return result
      def set_active(self, act):
            self.__active = act
      def isActive():
            return sefl.__active
##      def display(self):
##            print (self.
      """
            MAIN FUNCTION
      """
      def main():
            account1 = BankAccount()
            account2 = BankAcount(234, 876904899, "Miley", 2000.00)
            account3 = BankAccount(456, 334354546, "Amanda", "Robins", 6000.00)
            
            print(account1, "\n\n\n", account2, "\n\n\n", account3)

            if isActive():
                  deposit(account1, 500)
                  deposit(account2, 600)
                  deposit(account3, 20)
            else: print("not active")

            print(account1, "\n\n\n", account2, "\n\n\n", account3)

            set_active(account1, True)
            set_active(account2, Active)

            withdraw(account1, 10)
            withdraw(account2, 20)
            withdraw(account3,200)

            print(account1, "\n\n\n", account2, "\n\n\n", account3)

main()

            

            
      
