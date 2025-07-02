# Task 3
# balance_checker.py	Simulate login + account number validation	while, list, validation
# password_validator.py	Validate password rules	if, string functions
# transaction_history.py
num_customer = int(input("Enter the number of customers: "))
for i in range(1, num_customer + 1):
    print(f"\n Customer {i}")

    inital_balance = float(input("Enter initial balance: "))
    annual_interest_rate = float(input("Enter annual interest rate: "))
    years = int(input("Enter the number of years: "))

    future_balance = inital_balance * ((1 + annual_interest_rate / 100) ** years)
    print(f"Future balance after {years} years: {future_balance}")
