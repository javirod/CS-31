####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Chapter 5 Homework
# Due Date: 28 MAR 2021
####################################################
import random

########## Problem 17 and 18, Prime Numbers ##########
def is_prime(num):
    if num ==  0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

########## Problem 19, Future Value ##########
def futValue(amount, interest, time):
    return amount * (1 + interest) ** time

def main():
    ########## Problem 17 and 18, Prime Numbers ##########
    print("\n########## Problem 17 and 18, Prime Numbers ##########")
    print("--------------------------------------------------")
    for x in range(100):
        primeCheck = is_prime(x)
        if primeCheck:
            print(x, end = " ")
    print()
    print()
    ########## Problem 19, Future Value ##########
    print("\n########## Problem 19, Future Value ##########")
    print("--------------------------------------------------")
    presentValue = int(input("Please enter the present value: "))
    interestRate = float(input("Please enter the monthly interest rate: "))
    months = int(input("Please enter the months that the money will be left in the account: "))
    futureValue = futValue(presentValue, interestRate, months)
    print(f'The future value will be ${futureValue:.2f}')
    print()
    print()
    ########## Problem 21, Rock, Paper, Scissors Game ##########
    print("\n########## Problem 21, Rock, Paper, Scissors Game ##########")
    print("--------------------------------------------------")
    playAgain = 'y'
    while (playAgain == 'y') or (playAgain == 'Y'):
        compChoice = random.randrange(1,4)
        playerChoice = int(input("Please enter 1 for Rock, 2 for Paper, and 3 for Scissors: "))
        if compChoice == 1:
            print(f'The computer chose: Rock')
        elif compChoice == 2:
            print(f'The computer chose: Paper')
        elif compChoice == 3:
            print(f'The computer chose: Scissors')
        print()
        if playerChoice == compChoice:
            print("Draw, play again to determine the winner.")
        elif playerChoice < 1 or playerChoice > 3:
            print("Invalid choice. Computer wins.")
        elif (playerChoice == 1 and compChoice == 3) or (playerChoice == 2 and compChoice == 1) or (playerChoice == 3 and compChoice == 2):
            print("You Win!!!")
        elif (playerChoice == 1 and compChoice == 2) or (playerChoice == 2 and compChoice == 3) or (playerChoice == 3 and compChoice == 1):
            print("You Lose!!!")
        playAgain = input("Would you like to play again? (y/n): ")
        print()

main()