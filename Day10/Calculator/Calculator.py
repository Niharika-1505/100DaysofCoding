from replit import clear
from art import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def division(a, b):
    if a == 0 or b == 0:
        return "Error: Divide by Zero Exception"
    return a / b


def multiply(a, b):
    return a * b


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}

new_Calculation = False
while not new_Calculation:
    print(logo)
    calculation_end = False
    value1 = float(input("what is the first number:"))
    while not calculation_end:

        operator = str(input("Please chose an operator + - * /: "))
        if operator in operators:
            value2 = float(input("what is the next number:"))
            calculation_function = operators[operator]
            res = calculation_function(value1, value2)
            print(f"{value1} {operator} {value2} = {res}")

            restart = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ")
            if restart.lower() == "y":
                value1 = res
            elif restart.lower() == "n":
                calculation_end = True
                clear()
        else:
            print("Please enter a valid operator")
    restart = input("Type 'y' to start a new calculation. Otherwise type 'n':\n")
    if restart.lower() == "n":
        new_Calculation = True
        clear()
        print("Calculator program terminated")