####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Chapter 4 Homework
# Due Date: 07 MAR 2021
####################################################

########## Problem 12, Calculating the Factorial of a Number ##########
print("\n########## Problem 12, Calculating the Factorial of a Number ##########")
print("--------------------------------------------------")
number = int(input("Please enter a positive integer: "))
factorial = 1
if number < 0:
    print("Error: Number entered is invalid.")
elif number == 0:
    print(f'Factorial of {number} is 1')
else:
    for x in range(1, number + 1):
        factorial *=  x
    print(f'Factorial of {number} is {factorial:,}')
print()

########## Problem 13, Population ##########
# Questions: Will input have perecent symbol for rate and can formatting be only 2 decimal places for population in table.
print("\n########## Problem 13, Population ##########")
organisms = int(input("Please enter the starting number of organisms: "))
rate = int(input("Please enter the average daily population increase as a percentage: "))
days = int(input("Please enter the number of days the organisms will be left to multiply: "))
rate = rate/100
print(rate)
print("\nDay Approximate\t\tPopulation")
print(f'1\t\t\t{organisms:,.6f}')
for x in range(2, days + 1):
    organisms = organisms * (1 + rate)
    print(f'{x}\t\t\t{organisms:,.6f}')
print()

########## Problem 15, Nested Loop Pattern ##########
print("\n########## Problem 15, Nested Loop Pattern ##########\n")
numLines = 6
for x in range(1, numLines + 1):
    print("#", end = "")
    for y in range(0,x-1):
        print(" ", end = "")
    print("#")
print()