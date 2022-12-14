# TC: O(1), SC: O(1)
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
            self.print_line()
            print("Low balance!")
            return False
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.valid_account(account):
            self.balance[account-1] += money
            self.print_line()
            print(f"Deposited ${money} to account{account}! \nCurrent balance is ${self.balance[account-1]}.")
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.valid_account(account):
            if self.valid_balance(account, money):
                self.balance[account-1] -= money
                self.print_line()
                print(f"Withdrew ${money} from account{account}! \nCurrent balance is ${self.balance[account-1]}.")
                return True
            self.print_line()
            print("Low balance!")
            return False
        return False
    
    def valid_account(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def valid_balance(self, account: int, money: int) -> bool:
        return self.balance[account-1] >= money

    def print_line(self) -> str:
        print("--------------------------------------------")


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

"""
Input
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]

Output
[null, true, true, true, false, false]

Stdout
--------------------------------------------
Withdrew $10 from account3! 
Current balance is $10.
--------------------------------------------
Transferred $20 from account5 to account1!                 
Current balance of the account5 is $10.                
Current balance of the account1 is $30.
--------------------------------------------
Deposited $20 to account5! 
Current balance is $30.
--------------------------------------------
Low balance!
"""