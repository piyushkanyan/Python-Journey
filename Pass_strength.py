# Password Strength Checker
Password = input("Enter the Password: ")

if len(Password) < 6:
    print(f"Your Password can't be less than 6 characters")
elif Password.find(" ") != -1:
    print("Your Password can't contain space")
elif Password.isalpha() != -1:
    print("Your Password can't contain number")
