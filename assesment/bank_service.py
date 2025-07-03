
from service.interfaces import IBankServiceProvider
from service.customer_service import CustomerServiceProviderImpl
from entity.account import Account
from entity.customer import Customer
from entity.transaction import Transaction
from typing import List

class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name: str, branch_address: str):
        super().__init__()
        self.accountList: List[Account] = []
        self.transactionList: List[Transaction] = []
        self.branchName = branch_name
        self.branchAddress = branch_address

    def create_account(self, customer: Customer, accNo: int, accType: str, balance: float) -> Account:
        account = Account(accNo, customer.customer_id, accType, balance)
        self.accountList.append(account)
        self.accounts[accNo] = account
        return account

    def list_accounts(self) -> List[Account]:
        return self.accountList

    def calculate_interest(self) -> None:
        for account in self.accountList:
            if account.account_type.lower() == "savings":
                interest = account.balance * 0.045  # 4.5% interest
                account.balance += interest
