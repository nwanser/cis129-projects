# CIS129_YourLastName_Lab5.py
# Natalia
# Date: October 15, 2024
# Lab 5: The Bottle Return Program
# This program calculates the total number of bottles collected and the payout for a week,
# then offers to run again for another week's data.

def main():
    """The main function to run the Bottle Return program."""
    keep_going = 'y'

    while keep_going.lower() == 'y':
        total_bottles = get_bottles()
        total_payout = calc_payout(total_bottles)
        print_info(total_bottles, total_payout)
        keep_going = input('Do you want to run the program again? (Enter y or n): ')

def get_bottles():
    """Function to get the number of bottles returned for a week."""
    total_bottles = 0
    for day in range(1, 8):  # From day 1 to 7
        today_bottles = int(input(f'Enter number of bottles for day #{day}: '))
        total_bottles += today_bottles
    return total_bottles

def calc_payout(total_bottles):
    """Function to calculate the payout based on the total number of bottles."""
    return total_bottles * 0.10

def print_info(total_bottles, total_payout):
    """Function to print out the total bottles collected and the payout."""
    print(f'The total number of bottles collected is {total_bottles}')
    print(f'The total paid out is ${total_payout:.2f}')

if __name__ == "__main__":
    main()
