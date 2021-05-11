####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Project 2
# Due Date: 09 MAY 2021
####################################################

def main():
    print("\n/*/*/*/*/*/*/*/*/*/ Binary Burgers Order Program /*/*/*/*/*/*/*/*/*/\n")
    numOrders = int(input("How many orders would you like to make: "))
    while numOrders < 1:
        numOrders = input("How many orders would you like to make: ")
    
    for x in range(1, numOrders+1):
        print(f'\n**********~~~~~~~~~~ Processing Order #{x} **********~~~~~~~~~~')
        sandwichSelected, sandwichPrice = selectSandwich()
        sideSelected, sidePrice = selectSide()
        drinkSelected, drinkPrice, sizeSelected = selectDrink()
        storeOrders(x, sandwichSelected, sandwichPrice, sideSelected, sidePrice, drinkSelected, sizeSelected, drinkPrice)

def selectSandwich():
    HAMBURGER = 2.75
    CHEESEBURGER = 3.25
    CHICKEN_SANDWICH = 2.50
    print("For a hamburger select 1\tFor a cheeseburger select 2\tFor a chicken sandwhich select 3\tFor no sandwich select 4.")
    sandwich = int(input("Please select a sandwich: "))
    while sandwich < 1 or sandwich > 4:
        print('Invalid selection. Please try again.')
        sandwich = int(input("Please select a sandwich: "))
    if sandwich == 1:
        return "Hamburger", HAMBURGER
    elif sandwich == 2:
        return "Cheeseburger", CHEESEBURGER
    elif sandwich == 3:
        return "Chicken Sandwich", CHICKEN_SANDWICH
    else:
        return -1, 0

def selectSide():
    FRENCH_FRIES = 2.25
    ONION_RINGS = 1.75
    SALAD = 1.50 
    print("\nFor french fries select 1\tFor onion rings select 2\tFor a side salad select 3\tFor no side select 4.")
    side = int(input("Please select a side: "))
    while side < 1 or side > 4:
        print('Invalid selection. Please try again.')
        side = int(input("Please select a side: "))
    if side == 1:
        return "French Fries", FRENCH_FRIES
    elif side == 2:
        return "Onion Rings", ONION_RINGS
    elif side == 3:
        return "Side Salad", SALAD
    else:
        return -1, 0

def selectDrink():
    SMALL = 1.50
    MEDIUM = 2.25
    LARGE = 2.75
    WATER = 0
    print("\nFor Coke select 1\tFor Sprite select 2\tFor Lemonade select 3\tFor a cup of water select 4.")
    drink = int(input("Please select a drink: "))
    while drink < 1 or drink > 4:
        print('Invalid selection. Please try again.')
        drink = int(input("Please select a drink: "))
    if drink > 0 and drink < 4:
        print("\nFor a Small drink select 1\tFor a Medium drink select 2\tFor a Large drink select 3.")
        drinkSize = int(input("Please select a drink size: "))
        while drinkSize < 1 or drinkSize > 3:
            print('Invalid selection. Please try again.')
            drinkSize = int(input("Please select a drink size: "))
    if drink == 1:
        if drinkSize == 1:
            return "Coke", SMALL, "Small"
        elif drinkSize == 2:
            return "Coke", MEDIUM, "Medium"
        elif drinkSize == 3:
            return "Coke", LARGE, "Large"
    elif drink == 2:
        if drinkSize == 1:
            return "Sprite", SMALL, "Small"
        elif drinkSize == 2:
            return "Sprite", MEDIUM, "Medium"
        elif drinkSize == 3:
            return "Sprite", LARGE, "Large"
    elif drink == 3:
        if drinkSize == 1:
            return "Lemonade", SMALL, "Small"
        elif drinkSize == 2:
            return "Lemonade", MEDIUM, "Medium"
        elif drinkSize == 3:
            return "Lemonade", LARGE, "Large"
    elif drink == 4:
        return "Water", WATER, -1

def storeOrders(orderNum, sandwichSelected, sandwichPrice, sideSelected, sidePrice, drinkSelected, sizeSelected, drinkPrice):
    subtotal = sandwichPrice + sidePrice + drinkPrice
    drinkName = f'{sizeSelected} {drinkSelected}'
    SALES_TAX = .08
    tax = subtotal * SALES_TAX
    total = subtotal + tax
    if orderNum == 1:
        outfile = open('order.txt', 'w')
    else:
        outfile = open('order.txt', 'a')
    outfile.write(f'\n**********~~~~~~~~~~ Total for Order #{orderNum} **********~~~~~~~~~~\n')
    if sandwichSelected != -1:
        outfile.write(f'{sandwichSelected:20}${sandwichPrice:.2f}\n')
    if sideSelected != -1:
        outfile.write(f'{sideSelected:20}${sidePrice:.2f}\n')
    if drinkSelected == 'Water':
        outfile.write(f'{drinkSelected:20}${drinkPrice:.2f}\n')
    else:
        outfile.write(f'{drinkName:20}${drinkPrice:.2f}\n')
    outfile.write('-----------------------------\n')
    outfile.write(f'{"Subtotal:":20}${subtotal:.2f}\n')
    outfile.write(f'{"Sales Tax:":20}${tax:.2f}\n')
    outfile.write(f'{"Total:":20}${total:.2f}\n')
    outfile.close()

main()