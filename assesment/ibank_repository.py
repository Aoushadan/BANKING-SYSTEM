

from abc import ABC, abstractmethod
from datetime import date
from typing import List
from entity.customer import Customer
from entity.account import Account
from entity.transaction import Transaction

class IBankRepository(ABC):
    @abstractmethod
    def create_account(self, customer: Customer, accNo: int, accType: str, balance: float) -> None:
        pass

    @abstractmethod
    def list_accounts(self) -> List[Account]:
        pass

    @abstractmethod
    def calculate_interest(self) -> None:
        pass

    @abstractmethod
    def get_account_balance(self, account_number: int) -> float:
        pass

    @abstractmethod
    def deposit(self, account_number: int, amount: float) -> float:
        pass

    @abstractmethod
    def withdraw(self, account_number: int, amount: float) -> float:
        pass

    @abstractmethod
    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> None:
        pass

    @abstractmethod
    def get_account_details(self, account_number: int) -> str:
        pass

    @abstractmethod
    def get_transactions(self, account_number: int, from_date: date, to_date: date) -> List[Transaction]:
        pass
