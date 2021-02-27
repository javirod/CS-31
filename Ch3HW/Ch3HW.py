####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Chapter 3 Homework
# Due Date: 28 FEB 2021
####################################################

########## Problem 7, Color Mixer ##########
print("\n########## Problem 7, Color Mixer ##########")
print("--------------------------------------------------")
color1 = input("Please enter a primary color (red, blue, or yellow): ")
color2 = input("Please enter a different primary color: ")

if (color1 != 'red' and color1 != 'blue' and color1 != 'yellow') or (color2 != 'red' and color2 != 'blue' and color2 != 'yellow'):
    print("Error: You have entered a non-primary color.")
elif color1 == color2:
    print("Error: You have entered the same color twice.")
elif (color1 == 'red' and color2 == 'blue') or (color2 == 'red' and color1 == 'blue'):
    print("You have made the secondary color, purple")
elif (color1 == 'red' and color2 == 'yellow') or (color2 == 'red' and color1 == 'yellow'):
    print("You have made the secondary color, orange")
elif (color1 == 'blue' and color2 == 'yellow') or (color2 == 'blue' and color1 == 'yellow'):
    print("You have made the secondary color, green")
print()

########## Problem 9, Roulette Wheel Colors ##########
print("\n########## Problem 9, Roulette Wheel Colors ##########")
print("--------------------------------------------------")
pocket = int(input("Please enter a pocket number (0 to 36, inclusive): "))

if pocket < 0 or pocket > 36:
    print("You have entered an invalid pocket number.")
elif pocket == 0:
    print("Pocket color is green.")
elif pocket <= 10:
    if pocket % 2 == 1:
        print("Pocket color is red.")
    else:
        print("Pocket color is black.")
elif pocket <= 18:
    if pocket % 2 == 1:
        print("Pocket color is black.")
    else:
        print("Pocket color is red.")
elif pocket <= 28:
    if pocket % 2 == 1:
        print("Pocket color is red.")
    else:
        print("Pocket color is black.")
elif pocket <= 36:
    if pocket % 2 == 1:
        print("Pocket color is black.")
    else:
        print("Pocket color is red.")
print()

########## Problem 12, Software Sales ##########
print("\n########## Problem 12, Software Sales ##########")
print("--------------------------------------------------")
PRICE = 99
quantity = int(input("Please enter number of packages purchased: "))

if quantity < 1:
    print("Error: Invalid quantity.")
elif quantity < 10:
    print("No discount is given.")
    total = PRICE * quantity
    print(f'Your total is ${total:,.2f}')
elif quantity < 20:
    subtotal = PRICE * quantity
    DISCOUNT = .10
    disc_amount = subtotal * DISCOUNT
    total = subtotal - disc_amount
    print(f'A discount of {DISCOUNT*100:.0f}% saves you ${disc_amount:,.2f}')
    print(f'Your total is ${total:,.2f}')
elif quantity < 50:
    subtotal = PRICE * quantity
    DISCOUNT = .20
    disc_amount = subtotal * DISCOUNT
    total = subtotal - disc_amount
    print(f'A discount of {DISCOUNT*100:.0f}% saves you ${disc_amount:,.2f}')
    print(f'Your total is ${total:,.2f}')
elif quantity < 100:
    subtotal = PRICE * quantity
    DISCOUNT = .30
    disc_amount = subtotal * DISCOUNT
    total = subtotal - disc_amount
    print(f'A discount of {DISCOUNT*100:.0f}% saves you ${disc_amount:,.2f}')
    print(f'Your total is ${total:,.2f}')
else:
    subtotal = PRICE * quantity
    DISCOUNT = .40
    disc_amount = subtotal * DISCOUNT
    total = subtotal - disc_amount
    print(f'A discount of {DISCOUNT*100:.0f}% saves you ${disc_amount:,.2f}')
    print(f'Your total is ${total:,.2f}')
print()