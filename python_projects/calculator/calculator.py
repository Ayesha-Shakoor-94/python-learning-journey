from typing import Union

# Function to perform addition
def add(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 + num2

# Function to perform subtraction
def subtract(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 - num2

# Function to perform multiplication
def multiply(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 * num2

# Function to perform division
def divide(num1: Union[int, float], num2: Union[int, float]) -> float:
    return num1 / num2

# Function to perform modulus operation
def modulus(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 % num2

# Function to perform exponentiation
def exponentiation(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 ** num2

# Function to perform floor division
def floordivision(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 // num2

# Main function to perform calculations
def calculate() -> None:
    while True:
        print('''
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
5 - Modulus
6 - Exponentiation
7 - Floor Division  
8 - Exit
'''     
        )
        # User input for choice of operation
        choice = int(input('Select the operation (1-8): '))
        
        # Exit the loop if the user chooses to exit
        if choice == 8:
            print("Exiting the calculator. Goodbye!")
            break

        # Check if the choice is valid and prompt user for numbers
        if choice in [1, 2, 3, 4, 5, 6, 7]:
            num1: Union[int, float] = int(input('Enter the first number: '))
            num2: Union[int, float] = int(input('Enter the second number: '))

            # Perform the selected operation and display the result
            if choice == 1:
                result = add(num1, num2)
                print(f"Your result is: {result}")
            elif choice == 2:
                result = subtract(num1, num2)
                print(f"Your result is: {result}")
            elif choice == 3:
                result = multiply(num1, num2)
                print(f"Your result is: {result}")
            elif choice == 4:
                result = divide(num1, num2)
                print(f"Your result is: {result}")
            elif choice == 5:
                result = modulus(num1, num2)
                print(f"Your result is: {result}")
            elif choice == 6:
                result = exponentiation(num1, num2)
                print(f"Your result is: {result}")
            elif choice == 7:
                result = floordivision(num1, num2)
                print(f"Your result is: {result}")
        else:
            # Handle invalid choice
            print('Invalid operation. Please choose a number between 1 and 8.')

# Run the calculator function
calculate()
