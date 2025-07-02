# Task 2

balance = float(input("Enter your current balance: "))

print("Choose a transaction to perform")
print("1. Check balance")
print("2. Withdraw")
print("3. Deposit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print(f"Your current balance is: {balance}")

elif choice == 2:
    withdraw_amount = float(input("Enter amount to withdraw (multiples of 100 or 500): "))
    if withdraw_amount > balance:
        print("Transaction failed: Insufficient Balance")
    elif withdraw_amount % 100 != 0 and withdraw_amount % 500 != 0:
        print("Transaction failed: Amount not in multiples of 100 or 500")
    else:
        balance = balance - withdraw_amount
        print(f"Withdrawal successful. New balance: {balance}")

elif choice == 3:
    deposit_amount = float(input("Enter amount to deposit: "))
    if deposit_amount <= 0:
        print("Deposit amount must be greater than zero.")
    else:
        balance = balance + deposit_amount
        print(f"Deposit successful. New balance: {balance}")

else:
    print("Invalid choice.")


