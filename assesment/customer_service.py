
from service.interfaces import ICustomerServiceProvider
from entity.account import Account

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}  # Simulated account storage

    def get_account_balance(self, account_number: int) -> float:
        account = self.accounts.get(account_number)
        if not account:
            raise Exception("Account not found.")
        return account.balance

    def deposit(self, account_number: int, amount: float) -> float:
        account = self.accounts.get(account_number)
        if not account:
            raise Exception("Account not found.")
        account.balance += amount
        return account.balance

    def withdraw(self, account_number: int, amount: float) -> float:
        account = self.accounts.get(account_number)
        if not account:
            raise Exception("Account not found.")
        if account.balance < amount:
            raise Exception("Insufficient balance.")
        account.balance -= amount
        return account.balance

    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> None:
        self.withdraw(from_account_number, amount)
        self.deposit(to_account_number, amount)

    def get_account_details(self, account_number: int) -> str:
        account = self.accounts.get(account_number)
        if not account:
            raise Exception("Account not found.")
        return str(account)
