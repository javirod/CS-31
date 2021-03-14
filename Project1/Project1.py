####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Project 1
# Due Date: 21 MAR 2021
####################################################

HAMBURGER = 2.75
CHEESEBURGER = 3.25
CHICKEN_SANDWICH = 2.50
FRENCH_FRIES = 2.25
ONION_RINGS = 1.75
SALAD = 1.50
SMALL = 1.50
MEDIUM = 2.25
LARGE = 2.75
WATER = 0
SALES_TAX = .08
subtotal = 0
print("\n/*/*/*/*/*/*/*/*/*/ Binary Burgers Order Program /*/*/*/*/*/*/*/*/*/\n")
print("For a hamburger select 1\tFor a cheeseburger select 2\tFor a chicken sandwhich select 3\tFor no sandwich select 4.")
sandwich = int(input("Please select a sandwich: "))

print("\nFor french fries select 1\tFor onion rings select 2\tFor a side salad select 3\tFor no side select 4.")
side = int(input("Please select a side: "))

print("\nFor Coke select 1\tFor Sprite select 2\tFor Lemonade select 3\tFor a cup of water select 4.")
drink = int(input("Please select a drink: "))

if drink >= 1 and drink <= 3:
    print("\nFor a Small drink select 1\tFor a Medium drink select 2\tFor a Large drink select 3.")
    drink_size = int(input("Please select a drink size: "))
    if drink_size < 1 or drink_size > 3:
        drink_size = 2

print("\nHere is your order:\n")

if sandwich == 1:
    print(f'{"Hamburger":20}${HAMBURGER:.2f}')
    subtotal = subtotal + HAMBURGER
elif sandwich == 2:
    print(f'{"Cheeseburger":20}${CHEESEBURGER:.2f}')
    subtotal = subtotal + CHEESEBURGER
elif sandwich == 3:
    print(f'{"Chicken Sandwich":20}${CHICKEN_SANDWICH:.2f}')
    subtotal = subtotal + CHICKEN_SANDWICH

if side == 1:
    print(f'{"French Fries":20}${FRENCH_FRIES:.2f}')
    subtotal = subtotal + FRENCH_FRIES
elif side == 2:
    print(f'{"Onion Rings":20}${ONION_RINGS:.2f}')
    subtotal = subtotal + ONION_RINGS
elif side == 3:
    print(f'{"Side Salad":20}${SALAD:.2f}')
    subtotal = subtotal + SALAD

if drink < 1 or drink >= 4:
    print(f'{"Water":20}${WATER:.2f}')
elif drink == 1 and drink_size == 1:
    print(f'{"Small Coke":20}${SMALL:.2f}')
    subtotal = subtotal + SMALL
elif drink == 1 and drink_size == 2:
    print(f'{"Medium Coke":20}${MEDIUM:.2f}')
    subtotal = subtotal + MEDIUM
elif drink == 1 and drink_size == 3:
    print(f'{"Large Coke":20}${LARGE:.2f}')
    subtotal = subtotal + LARGE
elif drink == 2 and drink_size == 1:
    print(f'{"Small Sprite":20}${SMALL:.2f}')
    subtotal = subtotal + SMALL
elif drink == 2 and drink_size == 2:
    print(f'{"Medium Sprite":20}${MEDIUM:.2f}')
    subtotal = subtotal + MEDIUM
elif drink == 2 and drink_size == 3:
    print(f'{"Large Sprite":20}${LARGE:.2f}')
    subtotal = subtotal + LARGE
elif drink == 3 and drink_size == 1:
    print(f'{"Small Lemonade":20}${SMALL:.2f}')
    subtotal = subtotal + SMALL
elif drink == 3 and drink_size == 2:
    print(f'{"Medium Lemonade":20}${MEDIUM:.2f}')
    subtotal = subtotal + MEDIUM
elif drink == 3 and drink_size == 3:
    print(f'{"Large Lemonade":20}${LARGE:.2f}')
    subtotal = subtotal + LARGE

tax = subtotal * SALES_TAX
total =  subtotal + tax
print("-----------------------------")
print(f'{"Subtotal:":20}${subtotal:.2f}')
print(f'{"Sales Tax:":20}${tax:.2f}')
print(f'{"Total:":20}${total:.2f}\n')