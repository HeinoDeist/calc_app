# Task 1
# The programme gives the user a menu and options to do a maths operation, print history or quit. 

num1 = 0
num2 = 0
answer = 0
operation = ""

# Function does the calculation in sequence of numbers received as arguments, i.e.: if num1 is entered first it will become the numerator in a division operation. 
def math_operation(num1,num2,operation):

    if operation =="*":
        answer = num1 * num2

    elif operation == "+":
        answer = num1 + num2

    elif operation == "-":
        answer = num1 - num2

    elif operation =="/":
        answer = num1 / num2

    return answer

# Function asks the user for input and requires no arguments. Returns the two numbers and the mathematical operation. 
def user_input():
    
    op_list = ["*" , "/" , "+" , "-"]
    operation = ""
    
    # Checks for valid numerical entry. Used "Exception" because errors can be quite broad. 
    while True:
        try:
            num1 = float(input("Please enter a number:"))
            break
        except Exception:
            print("Not a valid number. Please re-enter a valid number: ")
    
    # Checks for valid operators.
    while not operation in op_list:
        operation = str(input("Please enter an operation to be performed ( * , / , + , - "")"": "))
        if not operation in op_list:
            print("Please enter a valid operator:")

    # Checks for valid numerical entry. Used "Exception" because errors can be quite broad.
    while True:
        try:
            num2 = float(input("Please enter the second number: "))
            break
        except Exception:
            print("Not a valid number. Please re-enter a valid number: ")

    return num1, num2, operation


# Function asks user for menu options and returns the choice letter (a,b,c).
def user_menu():

    print("Option Menu:")
    print("a - Perform a maths operation on two numbers")
    print("b - Print historical maths operations")
    print("c - Quit")

    choice_list = ["a" , "b" , "c"]
    choice = ""

    # Loops checks if a valid menu option has been selected. 
    while not choice in choice_list:
        choice = str(input("Please enter your selection: "))
        if not choice in choice_list:
            print("Please enter a valid option. Inputs are case sensitive.")
    return choice

menu_choice = user_menu()

# Loop runs continuously as long as the user does not select the exit option (c). 
while menu_choice != "c":
    
    # Menu option performs and print maths operation and appends to file. 
    if menu_choice == "a":
        
        num1, num2, operation = user_input()
        answer = math_operation(num1,num2,operation)
        print(f"{num1:.2f} {operation} {num2:.2f} = {answer:.2f}") # Numbers formatted to two decimals. User might enter floats. 
        
        file = open("equations.txt", "a+")  # Creates a file if it does not exist. Creates in same directory. Reading and writing in append mode. 
        file.write(f"{num1:.2f} {operation} {num2:.2f} = {answer:.2f}\n")
        file.close()
        
        menu_choice = user_menu()

    # Menu option reads history from file and prints all the lines. 
    if menu_choice == "b":
        
        file = None 
        try:    
            file = open("equations.txt", "r")  # File is accessed in read mode. 
            for line in file:
                print(line.replace("\n",""))
        
        except FileNotFoundError as error:
            print("The file doe not exist. Select option 'a' to create new file.") # User might decide to go directly to option b, even before the file is created. Or file might have been deleted. 
        
        finally:
            if file is not None:
                file.close()
        
        menu_choice = user_menu()
