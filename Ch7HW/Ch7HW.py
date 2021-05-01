####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Chapter 7 Homework
# Due Date: 02 MAY 2021
####################################################
import os
import random
import matplotlib.pyplot as plt

def main():
    print('\n########## Problem 11, Lo Shu Magic Square ##########\n')
    magicSquare = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    if isMagicSquare(magicSquare):
        print('\nThe square is a Lo Shu Magic Square')
    else: print('\nThe square is NOT a Lo Shu Magic Square')
    
    magicEightBall()
    gasGraph()

########## Problem 11, Lo Shu Magic Square ##########
def isMagicSquare(magicList):
    column0 = magicList[0][0] + magicList[1][0] + magicList[2][0]
    column1 = magicList[0][1] + magicList[1][1] + magicList[2][1]
    column2 = magicList[0][2] + magicList[1][2] + magicList[2][2]
    row0 = magicList[0][0] + magicList[0][1] + magicList[0][2]
    row1 = magicList[1][0] + magicList[1][1] + magicList[1][2]
    row2 = magicList[2][0] + magicList[2][1] + magicList[2][2]
    diag0 = magicList[0][0] + magicList[1][1] + magicList[2][2]
    diag1 = magicList[2][0] + magicList[1][1] + magicList[0][2]
    print('Column 0:', column0, '\tColumn 1:', column1, '\tColumn 2:', column2)
    print('Row 0:', row0, '\tRow 1:', row1, '\tRow 2:', row2)
    print('Diagonal 0:', diag0, '\tDiagonal 1:', diag1)

    if column0 == 15 and column1 == 15 and column2 == 15 and row0 == 15 and row1 == 15 and row2 == 15 and diag0 == 15 and diag1 == 15:
        return True
    else:
        return False

########## Problem 13, Magic 8 Ball ##########
def magicEightBall():
    responses = []
    print('\n########## Problem 13, Magic 8 Ball ##########\n')
    infile = open('8_ball_responses.txt', 'r')
    responses = infile.readlines()
    infile.close()
    index = 0
    while index < len(responses):
        responses[index] = responses[index].rstrip('\n')
        index += 1
    repeat = 'y'
    while repeat == 'y' or repeat == 'Y':
        input('\nPlease enter a question for the Magic 8 Ball: ')
        indexResponse = random.randrange(0,12)
        print(responses[indexResponse])
        repeat = input('Would you like to ask another question? (y/n): ')

########## Problem 15, 1994 Weekly Gas Graph ##########
def gasGraph():
    infile = open('1994_Weekly_Gas_Averages.txt', 'r')
    gasPrices = infile.readlines()
    infile.close()
    index = 0
    while index < len(gasPrices):
        gasPrices[index] = float(gasPrices[index].rstrip('\n'))
        index += 1
        
    # Create lists with the X,Y coordinates of each data point.
    x_coords = list(range(1, 53))

    # Build the line graph.
    plt.plot(x_coords, gasPrices)

    # Add a title.
    plt.title('1994 Weekly Gas Prices')

    # Add labels to the axes.
    plt.xlabel('Week')
    plt.ylabel('Gas Prices')


    # Customize the tick marks.
    plt.xticks(list(range(0,53,4)),['0', '4', '8', '12', '16', '20', '24', '28', '32', '36', '40', '44', '48', '52'])
    plt.yticks([0.975, 1.000, 1.025, 1.050, 1.075, 1.100, 1.125, 1.150, 1.175],['$0.975', '$1.000', '$1.025', '$1.050', '$1.075', '$1.100', '$1.125', '$1.150', '$1.175'])

    # Add a grid.
    plt.grid(True)

    # Display the line graph.
    plt.show()

main()

