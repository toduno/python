# importing the random module
import random

# Define a function to check numbers
def check_number():
    
    # Let the players enter a number
    player_a_number = random.randint(1,10) # player a selects at random
    player_b_number = int(input('Enter a number from 1 - 10:')) # player b makes a guess

    # Add conditional statements to check if the two players numbers match 
    if (player_b_number <= 0 or player_b_number > 10):
        print('Number should be from 1 - 10')
    elif player_a_number == player_b_number:
        print('You win!')
    elif player_a_number != player_b_number:
        print('Try again!')    
        print('Hint: Number is between 1 - 10')
    else:
        print('You have not entered a number!')  

# Define an again() function so check_number() function can play again()
def again():
    calc_again = input('''
    Do you want to try again?
    Enter Y for YES or N for NO.
''') 

    if calc_again.upper() == 'Y':
        check_number()
    elif calc_again.upper() == 'N':
        print('Goodbye!')  
    else:
        again()

# Call the check_number() function
check_number()  

# Call the again() function after the check_number() function
again()

