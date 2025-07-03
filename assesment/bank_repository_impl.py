

import sqlite3
from datetime import datetime
from repository.ibank_repository import IBankRepository
from entity.customer import Customer
from entity.account import Account
from entity.transaction import Transaction
from typing import List
from util.db_conn_util import get_connection

class BankRepositoryImpl(IBankRepository):

    def create_account(self, customer: Customer, accNo: int, accType: str, balance: float) -> None:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Customers (customer_id, first_name, last_name, email, phone_number, address) VALUES (?, ?, ?, ?, ?, ?)",
                       (customer.customer_id, customer.first_name, customer.last_name, customer.email, customer.phone_number, customer.address))
        
        cursor.execute("INSERT INTO Accounts (account_id, customer_id, account_type, balance) VALUES (?, ?, ?, ?)",
                       (accNo, customer.customer_id, accType, balance))
        conn.commit()
        conn.close()

    def list_accounts(self) -> List[Account]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Accounts")
        rows = cursor.fetchall()
        conn.close()
        return [Account(*row) for row in rows]

    def calculate_interest(self) -> None:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT account_id, balance FROM Accounts WHERE account_type='savings'")
        accounts = cursor.fetchall()
        for acc_id, balance in accounts:
            interest = balance * 0.045
            cursor.execute("UPDATE Accounts SET balance = balance + ? WHERE account_id = ?", (interest, acc_id))
        conn.commit()
        conn.close()

    def get_account_balance(self, account_number: int) -> float:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM Accounts WHERE account_id = ?", (account_number,))
        row = cursor.fetchone()
        conn.close()
        return row[0] if row else 0.0

    def deposit(self, account_number: int, amount: float) -> float:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Accounts SET balance = balance + ? WHERE account_id = ?", (amount, account_number))
        conn.commit()
        return self.get_account_balance(account_number)

    def withdraw(self, account_number: int, amount: float) -> float:
        balance = self.get_account_balance(account_number)
        if balance < amount:
            raise Exception("Insufficient balance")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Accounts SET balance = balance - ? WHERE account_id = ?", (amount, account_number))
        conn.commit()
        return self.get_account_balance(account_number)

    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> None:
        self.withdraw(from_account_number, amount)
        self.deposit(to_account_number, amount)

    def get_account_details(self, account_number: int) -> str:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.first_name, c.last_name, a.account_type, a.balance
            FROM Customers c
            JOIN Accounts a ON c.customer_id = a.customer_id
            WHERE a.account_id = ?
        """, (account_number,))
        row = cursor.fetchone()
        conn.close()
        return f"Name: {row[0]} {row[1]}, Type: {row[2]}, Balance: ₹{row[3]}" if row else "Account not found."

    def get_transactions(self, account_number: int, from_date: datetime, to_date: datetime) -> List[Transaction]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM Transactions
            WHERE account_id = ? AND transaction_date BETWEEN ? AND ?
        """, (account_number, from_date, to_date))
        rows = cursor.fetchall()
        conn.close()
        return [Transaction(*row) for row in rows]
