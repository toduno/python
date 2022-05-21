# Create a welcome function to introduce the user to the calculate() function
def welcome():
    print('''
    Welcome to Calculator!
    What do you want to solve today?
    ''')

# Define the calculate() function
def calculate():
    
    # Prompt the user to put in an operation symbol
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    % for modulus
    ''')

    # Let the user enter two numbers
    num_1 = int(input('Please enter the first number: '))
    num_2 = int(input('Please enter the second number: '))

    # Add conditional statements so the calculate() function can run one operator at a time based on user's choice 
    if operation == '+':
        print('{} + {} ='.format(num_1, num_2))
        print(num_1 + num_2)

    elif operation == '-':
        print('{} - {} ='.format(num_1, num_2))
        print(num_1 - num_2)    

    elif operation == '*':
        print('{} * {} ='.format(num_1, num_2))
        print(num_1 * num_2) 

    elif operation == '/':
        print('{} / {} ='.format(num_1, num_2))
        print(num_1 / num_2)  

    elif operation == '%':
        print('{} % {} ='.format(num_1, num_2))
        print(num_1 % num_2) 

    else:
        print('You have not typed a valid operator, please run the program again.')

 # Define an again() function to calculate() function again()
def again():
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Goodbye!')
    else:
        again()

# Call the welcome() function 
welcome()

# Call calculate() outside of the function
calculate()

# Call again() after calculate() function 
again()
    