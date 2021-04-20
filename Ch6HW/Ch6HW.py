####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Chapter 6 Homework
# Due Date: 18 MAR 2021
####################################################
import os
import random

def main():
    try:
        averageNumbers()    # Problem 6 function
    except IOError:
        print('File did not open')
    except ValueError:
        print('Number could not be read')
    
    randomNumberWrite() # Problem 7 function
    randomNumberRead()  # Problem 8 function
    golfScoresWrite()   # Problem 10 function
    golfScoresRead()    # Problem 10 function

########## Problem 6 and 9, Average of Numbers ##########
def averageNumbers():
    sum = 0
    count = 0
    avgNumbers = 0
    infile = open('numbers.txt', 'r')
    for num in infile:
        num = float(num.rstrip('\n'))
        sum += num
        count += 1
    infile.close()
    avgNumbers = sum/count
    print(sum)
    print('\n########## Problem 6 and 9, Average of Numbers ##########\n')
    print(f'The average is {avgNumbers:.2f}')

########## Problem 7 and 8, Random Number File ##########
def randomNumberWrite():
    print('\n########## Problem 7 and 8, Random Number File ##########\n')
    countNum = int(input('Please enter how many numbers to write: '))
    outfile = open("randNumbers.txt", 'w')
    for x in range(0, countNum):
        numInput = random.randrange(1,501)
        outfile.write(f'{numInput}\n')
    outfile.close()

def randomNumberRead():
    count = 0
    sum = 0
    infile = open('randNumbers.txt', 'r')
    print()
    for num in infile:
        num = int(num.rstrip('\n'))
        print(num, '\n')
        count += 1
        sum += num
    infile.close()
    print(f'The total of the numbers is: {sum:,}')
    print(f'The number of random numbers read is: {count}\n')

########## Problem 10, Golf Scores ##########
def golfScoresWrite():
    sentScores = 'a'
    count = 0
    print('\n########## Problem 10, Golf Scores ##########\n')
    outfile = open("golf.txt", 'w')
    while(sentScores != 'q' and sentScores != 'Q'):
        count += 1
        print('Enter data for player #', count, sep='')
        name = input('Name: ')
        score = input('Score: ')
        outfile.write(name+'\n')
        outfile.write(score+'\n')
        sentScores = input('To enter more names click Enter, to quit enter "q": ')
    outfile.close()

def golfScoresRead():
    infile = open('golf.txt', 'r')
    print(f'\n{"Name":25}{"Score":5}')
    print('-----------------------------------')
    for name in infile:
        name = name.rstrip('\n')
        score = infile.readline().rstrip('\n')
        print(f'{name:25}{score:5}')
    infile.close()
    print()

main()