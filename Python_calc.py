repeat = "yes"
while repeat.lower() == "yes":
    print("===============================")
    print("         CALCULATOR            ")
    print("===============================")

    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    sign = input("Enter your choice (% ,+ ,- , * ,/ ): ")

    if sign == "%":
        print(f"Modulo of {number1} % {number2} is: {number1 % number2}")
    elif sign == "+":
        print(f"Addition of {number1} + {number2} is: {number1 + number2}")
    elif sign == "-":
        print(f"Subtraction of {number1} - {number2} is: {number1 - number2}")
    elif sign == "/":
        if number2 == 0:
            print("Division by zero is not allowed")
        else:
            print(f"Division of {number1} / {number2} is: {number1 / number2}")
    elif sign == "*":
        print(f"Multiplication of {number1} * {number2} is: {number1 * number2}")
    else:
        print("--> Please enter from this only (% ,+ ,- , * ,/ ) <--")

    repeat = input("Do you want to do another calculation? (yes or no): ").lower()
print("\n--->Thank you for using the calc<---")