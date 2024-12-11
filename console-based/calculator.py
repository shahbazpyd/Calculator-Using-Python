# Define functions for basic arithmetic operations.

def add(num1, num2):
    """
    This function takes two numbers as input and returns their sum.
    """
    return num1 + num2

def subtract(num1, num2):
    """
    This function takes two numbers as input and returns their difference.
    """
    return num1 - num2

def multiply(num1, num2):
    """
    This function takes two numbers as input and returns their product.
    """
    return num1 * num2

def divide(num1, num2):
    """
    This function takes two numbers as input and returns their quotient.
    """
    return num1 / num2


# Start an infinite loop to keep the calculator running until the user chooses to exit.
while True:
    # Display the menu of operations to the user.
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Get the user's choice of operation.
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    # If the user chooses to exit, break out of the loop.
    if choice == "5":
        break

    # Get the two numbers from the user.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the selected operation and print the result.
    if choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == "3":
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == "4":
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        # If the user enters an invalid choice, print an error message.
        print("Invalid choice. Please enter a number between 1 and 4.")

