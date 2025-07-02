# Task 4

account_numbers = { 101: 8500.75, 102: 15200.00, 103: 450.25, 104: 9999.99, 105: 12000.50}

while True:
    acc_no = int(input("Enter your account number: "))
    if acc_no in account_numbers:
        print(f"Account found. Your balance is {account_numbers[acc_no]}")
        break
    else:
        print("Invalid account number.")