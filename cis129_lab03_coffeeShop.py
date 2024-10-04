# Program: Coffee Shop Simulator (Extended)
# Description: A simple interactive text-based coffee shop simulator
#              that calculates the receipt based on customer input
# Author: [Your Name]
# Date: [Current Date]

# Constants
COFFEE_PRICE = 5.00
MUFFIN_PRICE = 4.00 
DOUGHNUT_PRICE = 2.50  # Replaced tea with doughnut
TEA_PRICE = 3.00       # Replaced pastry with tea
TAX_RATE = 0.06

# Input: Number of coffees, muffins, doughnuts, and teas the user is purchasing
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))
num_doughnuts = int(input("Number of doughnuts bought? "))  # Updated input prompt
num_teas = int(input("Number of teas bought? "))  # Updated input prompt

# Calculate subtotals
subtotal_coffee = num_coffees * COFFEE_PRICE
subtotal_muffin = num_muffins * MUFFIN_PRICE
subtotal_doughnut = num_doughnuts * DOUGHNUT_PRICE  # Updated calculation
subtotal_tea = num_teas * TEA_PRICE
subtotal = subtotal_coffee + subtotal_muffin + subtotal_doughnut + subtotal_tea  # Updated subtotal calculation

# Calculate tax
tax = subtotal * TAX_RATE

# Calculate total
total = subtotal + tax

# Output: Display the receipt
print("\n*******************************************")
print("Welcome to the Comfy Coffee Shop")
print("********************************************************************************")
print(f"{num_coffees} Coffee(s) at ${COFFEE_PRICE:.2f} each: ${subtotal_coffee:.2f}")
print(f"{num_muffins} Muffin(s) at ${MUFFIN_PRICE:.2f} each: ${subtotal_muffin:.2f}")
print(f"{num_doughnuts} Doughnut(s) at ${DOUGHNUT_PRICE:.2f} each: ${subtotal_doughnut:.2f}")  # Updated output
print(f"{num_teas} Tea(s) at ${TEA_PRICE:.2f} each: ${subtotal_tea:.2f}")
print(f"6% tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("********************************************************************************")
print("\nThank you for visiting Comfy Coffee Shop! We hope to see you again soon!")
