# ICA 1, Part 1
amount = float(input("Enter purchase amount: "))
STATE = 0.05
COUNTY = 0.025
state_tax = amount * STATE     # state sales tax
county_tax = amount * COUNTY   # county sales tax
total_tax = state_tax + county_tax
total_sale = amount + total_tax
print(f"Purchase Amount: ${amount:.2f}")
print(f"State Sales Tax: ${state_tax:.2f}")
print(f"County Sales Tax: ${county_tax:.2f}")
print("Total Sales Tax: $", format(total_tax, '.2f'), sep='')
print("Total Sale: $", format(total_sale, '.2f'), sep='')
print()
#8
check = float(input("How much was dinner? "))
TIP = 0.18
TAX = 0.07
tip = check * TIP
tax = check * TAX
total = check + tax + tip
print(f"Check amount: ${check:.2f}")
print(f"Sales Tax: ${tax:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")