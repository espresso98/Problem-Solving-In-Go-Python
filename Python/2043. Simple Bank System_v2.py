
class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.valid_account(account1) and self.valid_account(account2): 
            if self.valid_balance(account1, money): 
                self.balance[account1-1] -= money
                self.balance[account2-1] += money
                self.print_line()
                print(f"Transferred ${money} from account{account1} to account{account2}! \
                \nCurrent balance of the account{account1} is ${self.balance[account1-1]}.\
                \nCurrent balance of the account{account2} is ${self.balance[account2-1]}.")
                return True
            return False
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.valid_account(account):
            self.balance[account-1] += money
            self.print_line()
            print(f"Deposited ${money} to account{account}! \nCurrent balance account{account} is ${self.balance[account-1]}.")
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.valid_account(account):
            if self.valid_balance(account, money):
                self.balance[account-1] -= money
                self.print_line()
                print(f"Withdrew ${money} from account{account}! \nCurrent balance of account{account} is ${self.balance[account-1]}.")
                return True
            return False
        return False
    
    def valid_account(self, account: int) -> bool:
        if 1 <= account <= len(self.balance):
            return True
        else:
            self.print_line()
            print("Invalid account!")
            return False


    def valid_balance(self, account: int, money: int) -> bool:
        if self.balance[account-1] >= money:
            return True
        else:
            self.print_line()
            print("Low balance!")
            return False


    def print_line(self) -> str:
        print("--------------------------------------------")


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)


# --------------------------------------------
# Withdrew $10 from account3! 
# Current balance of account3 is $10.
# --------------------------------------------
# Transferred $20 from account5 to account1!                 
# Current balance of the account5 is $10.                
# Current balance of the account1 is $30.
# --------------------------------------------
# Deposited $20 to account5! 
# Current balance account5 is $30.
# --------------------------------------------
# Low balance!
# --------------------------------------------
# Invalid account!
