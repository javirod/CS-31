# Week 10, ICA 2
import os

def main():
    enterData()
    displayData()
    search()
    modifyNum()
    try:
        evens = 0
        odds = 0
        inf = open('numbers.txt', 'r')
        for num in inf:
            num = int(num)
            if num % 2 == 0:
                evens += 1
            else:
                odds += 1
        print('The file had', evens, 'evens and', odds, 'odds')
    except IOError:
        print('File did not open')
    except ValueError as duh:
        print(duh)
    finally:
        print('Moving on...')

def enterData():
    outfile = open("nba.txt", 'w')
    for x in range(1,4):
        print('Enter data for player #', x, sep='')
        name = input('Name: ')
        num = input('Number: ')
        team = input('Team: ')
        outfile.write(name+'\n')
        outfile.write(num+'\n')
        outfile.write(team+'\n')
    outfile.close()

def displayData():
    infile = open('nba.txt', 'r')
    for name in infile:
        name = name.rstrip('\n')
        num = infile.readline().rstrip('\n')
        team = infile.readline().rstrip('\n')
        print(name, 'wears number', num, 'and plays for the', team)
    infile.close()

def search():
    found = False
    infile = open('nba.txt', 'r')
    # Prompt user to enter a name of a player
    disone = input('Enter the name to search for: ')
    name = infile.readline().rstrip('/n')
    while name != '' and not found:
        num = infile.readline().rstrip('\n')
        team = infile.readline().rstrip('\n')
        if name == disone:
            print(name, 'wears number', num, 'and plays for the', team)
            found = True
        else:
            name = infile.readline().strip('\n')
    if not found:
        print(disone, 'is not in the file')
    infile.close()

def modifyNum():
    found = False
    disone = input('Enter the player to search for: ')
    newnum = input('Enter the new number: ')
    infile = open('nba.txt', 'r')
    temp = open('temp.txt', 'w')
    name = infile.readline().rstrip('\n')
    while name != '':
        num = infile.readline().rstrip('\n')
        team = infile.readline().rstrip('\n')
        if name == disone:
            temp.write(name+'\n')
            temp.write(newnum+'\n')
            temp.write(team+'\n')
            found = True
        else:
            temp.write(name+'\n')
            temp.write(num+'\n')
            temp.write(team+'\n')
        name = infile.readline().rstrip('\n')
    infile.close()
    temp.close()
    os.remove('nba.txt')
    os.rename('temp.txt', 'nba.txt')
    if found:
        print('File has been updated')
        displayData()
    else:
        print(disone, 'is not in the file')

main()