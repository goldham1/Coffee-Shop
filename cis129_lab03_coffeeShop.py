# Module 3 Lab 3
# Copyright Gabe Oldham, 2024
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 2  ----------------------------

#Create calculate total function that takes the number of coffees, muffins, donuts, and waffles.
#Calculates tax, subtotal, and total. Then prints a receipt.
def calculate_total(num_coffees, num_muffins, num_donuts, num_waffles):
    # Prices
    coffee_price = 5.00
    muffin_price = 4.00
    donut_price = 2.00
    waffle_price = 6.00
    tax_rate = 0.06

    # Calculate subtotal
    subtotal_coffees = num_coffees * coffee_price
    subtotal_muffins = num_muffins * muffin_price
    subtotal_donuts = num_donuts * donut_price
    subtotal_waffles = num_waffles * waffle_price
    subtotal = subtotal_coffees + subtotal_muffins + subtotal_donuts + subtotal_waffles

    # Calculate tax
    tax = subtotal * tax_rate

    # Calculate total
    total = subtotal + tax

    # Print order
    print("\n***************************************")
    print("Gabe's Cafe")
    print("Number of coffees bought?")
    print(num_coffees)
    print("Number of muffins bought?")
    print(num_muffins)
    print("Number of donuts bought?")
    print(num_donuts)
    print("Number of waffles bought?")
    print(num_waffles)
    print("***************************************")
    print("")

    #Print receipt
    print("***************************************")
    print("Gabe's Cafe Receipt")
    print(f"{num_coffees} Coffee{"" if num_coffees == 1 else "s"} at ${coffee_price:.0f} each: ${subtotal_coffees:.2f}")
    print(f"{num_muffins} Muffin{"" if num_muffins == 1 else "s"} at ${muffin_price:.0f} each: ${subtotal_muffins:.2f}")
    print(f"{num_donuts} Donut{"" if num_donuts == 1 else "s"} at ${donut_price:.0f} each: ${subtotal_donuts:.2f}")
    print(f"{num_waffles} Waffle{"" if num_waffles == 1 else "s"} at ${waffle_price:.0f} each: ${subtotal_waffles:.2f}")
    print(f"{int(tax_rate * 100)}% tax: $", f"{tax:.2f}".lstrip("0"))
    print("---------")
    print(f"Total: $ {total:.2f}")
    print("***************************************\n")

    #Print thank you
    print("***************************************")
    print("Thank you for stuffing your face at Gabe's Cafe!")
    print("***************************************\n")

#Gather inputs
num_coffees = int(input("How many coffees would you like?"))
num_muffins = int(input("How many muffins would you like?"))
num_donuts = int(input("How many donuts would you like?"))
num_waffles = int(input("How many waffles would you like?"))

#Run function
calculate_total(num_coffees, num_muffins, num_donuts, num_waffles)
