# Task 1

credit_score = int(input("Enter your credit score: "))
income = float(input("Enter your annual income: "))

if (credit_score > 700 and income >= 50000):
    print("Congratulation, You are eligible for loan.")
else:
    print("Sorry, you are not eligible for loan")
    