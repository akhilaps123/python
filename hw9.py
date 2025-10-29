class Account:
     def __init__(self,_name,_balance):
          self._name = _name
          self._balance = _balance
     def display_details(self):
          print(f"account_holder:{self._name} balance:{self._balance}")
     def __add__(self,other):
          return self._balance + other._balance
     
class SavingsAccount(Account):
     def __init__(self,_name,_balance):
          super().__init__(_name,_balance)
     def calculate_interest(self):
          return self._balance * 0.05
     
class CurrentAccount(Account):
     def __init__(self, _name, _balance):
          super().__init__(_name, _balance)
     def calculate_interest(self):
          return self._balance * 0.02
     
SavingsAcc = SavingsAccount("Ravi",10000)
CurrentAcc = CurrentAccount( "Anjali",15000)
SavingsAcc.display_details()
print("Interest (5%): ₹",SavingsAcc.calculate_interest())
CurrentAcc.display_details()
print("Interest (2%): ₹",CurrentAcc.calculate_interest())
total_balance = SavingsAcc + CurrentAcc
print("combined total balance:",total_balance)  

# You are helping a bank manage different types of bank accounts. Your task is to create a simple Python program that does the following steps in order:
# Create a base class called Account with an account holder's name (string) and balance (number, like 1000.0). Use a single underscore to keep the name and balance protected.
# Create a class called SavingsAccount that inherits from Account and has a method calculate_interest that returns the interest as balance * 0.05 (5% interest).
# Create a class called CurrentAccount that inherits from Account and has a method calculate_interest that returns the interest as balance * 0.02 (2% interest).
# Add a special method to the Account class so that using the + operator on two accounts adds their balances together.
# In the main part of the program:
# Create a SavingsAccount object for "Ravi" with a balance of 10000.
# Create a CurrentAccount object for "Anjali" with a balance of 15000.
# Show the name, balance, and interest for each account object.
# Show the total balance by adding the two account objects using the + operator.
# Make the output clear, showing each account’s name, balance, interest, and the total balance.

