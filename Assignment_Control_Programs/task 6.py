# Task 6

transactions = []

while True:
    print("Chhose your option: ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit and show transaction history")
    option = int(input("Enter your option: "))

    if option == 1:
        amount = float(input("Enter the amount to deposit: "))
        transactions.append(f"Deposited {amount}")
        print("transaction was recorded successfully.")
    elif option == 2:
        amount = float(input("Enter amount to withdraw: "))
        transactions.append(f"Withdrew {amount}")
        print("Transaction recorded successfully.")
    elif option == 3:
        print("Showing transaction history ")
        if not transactions:
            print("No transactions.")
        else:
            i = 1
            for t in transactions:
                print(f"{i}.{t}")
                i += 1
        print("Thank You ")
        break
    

        