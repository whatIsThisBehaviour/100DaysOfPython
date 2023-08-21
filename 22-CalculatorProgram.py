logo = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|'''

print(logo)

def sum(num1, num2):
    """return the addition value of two numbers"""
    return num1 + num2

def sub(num1, num2):
    """returns the subtraction value of two numbers"""
    return num1 - num2

def mul(num1, num2):
    """returns the multiplication value of two numbers"""
    return num1 * num2

def div(num1, num2):
    """returns the division value of two numbers"""
    return round(num1 / num2, 2)


operations = {
    "+" : sum,
    "-" : sub,
    "*" : mul,
    "/" : div,
}
def calculator():
    num1 = float(input("Enter the first number : "))

    for symbol in operations:
        print(symbol)


    should_continue = True
    while should_continue:

        operation_symbol = input("Pick the operation : ")

        num2 = float(input("Enter the next number : "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")


        if input(f"Type 'y' to continue calculating with {answer}, or type n to exit.: ")== "y":
            num1 = answer
        else:
            should_continue = False
            print(f"The final result is {answer}. Exiting the program.")

calculator()

