user_name = input('Please enter your name:')

# Define a welcome() function for the user 
def welcome():
    print('Welcome,', user_name)

    start_check = input('''
    Ready to detect your number?
    Please type Y for YES or N for NO.
    ''')

    if start_check.upper() == 'Y':
        print('''Let's go!''')
    elif start_check.upper() == 'N':
        print('Goodbye!')
    else:
        welcome()

# Call the welcome() function 
welcome()    

# Define a check_number() function to check for positive or negative number
def check_number():

    # Ask user to enter a number, `user_number`
    user_number = int(input('Please enter a number:'))
 
    # Make sure `user_number` is actually a number (validation)
    if user_number == int:
        print('You entered:', user_number)  

    # If the number is positive (user_number >= 0), print `True`
    if user_number >= 0:
        print(user_number, 'is a positive number')

    # Else, print `False` 
    else:
        print(user_number, 'is a negative number')

# Define an again() function to check_number() function again()
def again():
    check_again = input('''
    Do you want to check again?
    Please type Y for YES or N for NO.
    ''')

    if check_again.upper() == 'Y':
        check_number()
    elif check_again.upper() == 'N':
        print('Goodbye!')
    else:
        again()

# Call the check_number() function
check_number()

# Call the again() function after the check_number() function
again()