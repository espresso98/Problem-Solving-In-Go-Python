# O(1), O(1)
class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.valid_account(account1) and self.valid_account(account2): 
            if self.valid_balance(account1, money): 
                self.balance[account1-1] -= money
                self.balance[account2-1] += money
                return True
            return False
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.valid_account(account):
            self.balance[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.valid_account(account):
            if self.valid_balance(account, money):
                self.balance[account-1] -= money
                return True
            return False
        return False
    
    def valid_account(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def valid_balance(self, account: int, money: int) -> bool:
        return self.balance[account-1] >= money


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
