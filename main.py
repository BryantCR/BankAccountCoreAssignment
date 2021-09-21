from BankAccount import BankAccount
from User import User

juanUser = User("Juan", "Rodriguez", 35)
alvaroUser = User( "Alvaro", "Gomez", 38 )
juanUser.printUserInfo()

juanAccount = BankAccount(1.005, 10000, juanUser)
alvaroAccount = BankAccount(1.003, 5000, juanUser)

juanAccount.deposit(100).deposit(100).deposit(100).make_withdrawal(200).yield_interes(1.005).display_Account_Info()
alvaroAccount.deposit(100).deposit(100).make_withdrawal(200).make_withdrawal(150).make_withdrawal(200).make_withdrawal(150).yield_interes(1.003).display_Account_Info()
BankAccount.printAllAccountsInfo()