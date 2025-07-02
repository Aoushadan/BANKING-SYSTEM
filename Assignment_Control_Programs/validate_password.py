# Task 5
def valid_password(password):
    errors =[]
    if len(password) < 8:
        errors.append("Password must have atleast 8 characters.")
    if not any(char.isupper() for char in password):
        errors.append("Password must have atleast one uppercase letter.")
    if not any(char.isdigit() for char in password ):
        errors.append("Password must have atleast 1 digit.")

    return errors

while True:
    password = input("Please enter your password: ")
    validation_error = valid_password(password)

    if not validation_error:
        print("Password is valid. Account created successfully.")
        break
    else:
        print("\n".join(validation_error))
    