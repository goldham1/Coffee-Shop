# Module 3 Lab 3
# Copyright Gabe Oldham, 2024
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 1  ----------------------------

#Create calculate total function that takes the number of coffees and number of muffins 
#Calculates tax, subtotal, and total. Then prints a receipt.
def calculate_total(num_coffees, num_muffins):
    # Prices
    coffee_price = 5.00
    muffin_price = 4.00
    tax_rate = 0.06

    # Calculate subtotal
    subtotal_coffees = num_coffees * coffee_price
    subtotal_muffins = num_muffins * muffin_price
    subtotal = subtotal_coffees + subtotal_muffins

    # Calculate tax
    tax = subtotal * tax_rate

    # Calculate total
    total = subtotal + tax

    # Print order
    print("\n***************************************")
    print("My Coffee and Muffin Shop")
    print("Number of coffees bought?")
    print(num_coffees)
    print("Number of muffins bought?")
    print(num_muffins)
    print("***************************************")
    print("")

    #Print receipt
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(f"{num_coffees} Coffee{"" if num_coffees == 1 else "s"} at ${coffee_price:.0f} each: ${subtotal_coffees:.2f}")
    print(f"{num_muffins} Muffin{"" if num_muffins == 1 else "s"} at ${muffin_price:.0f} each: ${subtotal_muffins:.2f}")
    print(f"{int(tax_rate * 100)}% tax: $", f"{tax:.2f}".lstrip("0"))
    print("---------")
    print(f"Total: $ {total:.2f}")
    print("***************************************\n")

#Gather inputs
num_coffees = int(input("How many coffees would you like?"))
num_muffins = int(input("How many muffins would you like?"))

#Run function
calculate_total(num_coffees, num_muffins)
