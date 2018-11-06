# Project Simple Calculator version 0.1 Dawid B.

#  menu

while True:
    print("Options:")
    print("Enter 'add' to add two number")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("enter 'quit' to end the program")
    user_input = input(":")

    if user_input == "quit":
     break

    elif user_input == "add":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter second number"))
        print(num1+num2)
    elif user_input == "subtract":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter second number"))
        print(num1 - num2)
    elif user_input == "multiply":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter second number"))
        print(num1 * num2)
    elif user_input == "divide":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter second number"))
        print(num1 / num2)
    else:
        print("Unknown input")












