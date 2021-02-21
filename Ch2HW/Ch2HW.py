####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Chapter 2 Homework
# Due Date: 21 FEB 2021
####################################################

########## Problem 12, Stock Transaction Problem ##########
print("\n########## Problem 12, Stock Transaction Problem ##########\n")
SHARES_BOUGHT = 2000
STOCK_PRICE_BUY = 40
price_buy = SHARES_BOUGHT * STOCK_PRICE_BUY
COMMISSION_RATE = .03
commission_buy = price_buy * COMMISSION_RATE
SHARES_SOLD = 2000
STOCK_PRICE_SELL = 42.75
price_sell = SHARES_SOLD * STOCK_PRICE_SELL
commission_sell = price_sell * COMMISSION_RATE
net_gains = price_sell - price_buy - commission_buy - commission_sell
print(f"Joe bought his stock for: ${price_buy:.2f}")
print(f"Joe paid his broker a commission for the purchase: ${commission_buy:.2f}")
print(f"Joe sold his stock for: ${price_sell:.2f}")
print(f"Joe paid his broker a commission for the purchase: ${commission_sell:.2f}")
print(f"Joe's net gains are: ${net_gains:.2f}\n")

########## Problem 13, Planting Grapevines ##########
print("########## Problem 13, Planting Grapevines ##########\n")
row_length = float(input("Enter the length of the row in feet: "))
endpost_space = float(input("Enter the amount of space, in feet, used by an end-post assembly: "))
vine_space = float(input("Enter the space between vines in feet: "))
num_grapevines = (row_length - (2 * endpost_space)) / vine_space
print(f"The number of grapevines that will fit in the row are: {num_grapevines:.2f}\n")

########## Problem 14, Compound Interest ##########
print("########## Problem 14, Compound Interest ##########\n")
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate paid by the account: "))
rate = rate/100
compound = float(input("Enter the times per year compounded: "))
age = float(input("Enter the number of years that the account will earn interest: "))
total_amount = principal * (1 + (rate/compound)) ** (compound * age)
print(f"The amount of money that will be in the account after {age} year(s) is: ${total_amount:.2f}\n")