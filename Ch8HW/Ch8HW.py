####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Chapter 8 Homework
# Due Date: 09 MAY 2021
####################################################

def main():
    datePrinter()
    morseCode()
    alphaNumTranslator()

########## Problem 3, Date Printer ##########
def datePrinter():
    print('\n########## Problem 3, Date Printer ##########\n')
    dateInput = input('Please enter a date in the format MM/DD/YYYY:')
    dateList = dateInput.split('/')
    day = int(dateList[1])
    month = int(dateList[0])
    year = int(dateList[2])
    monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    print(f'{monthList[month-1]} {day}, {year}')

########## Problem 4, Morse Code Converter ##########
def morseCode():
    print('\n########## Problem 4, Morse Code Converter ##########\n')
    morseList = [[' ', ' '], [',', '– – . . – –'], ['.', '. – . – . –'], ['?', '. . – – . .'],
    ['1', '. _ _ _ _'], ['2', '. . _ _ _'], ['3', '. . . _ _'], ['4', '. . . . _'], ['5', '. . . . .'], 
    ['6', '_ . . . .'], ['7', '_ _ . . .'], ['8', '_ _ _ . .'], ['9', '_ _ _ _ .'], ['0', '_ _ _ _ _'],
    ['A', '. _'], ['B', '_ . . .'], ['C', '_ . _ .'], ['D', '_ . .'], ['E', '.'], ['F', '. . _ .'],
 	['G', '_ _ .'], ['H', '. . . .'], ['I', '. .'], ['J', '. _ _ _'], ['K', '_ . _'],
 	['L', '. _ . .'], ['M', '_ _'], ['N', '_ .'], ['O', '_ _ _'], ['P', '. _ _ .'], ['Q', '_ _ . _'],
    ['R', '. _ .'], ['S', '. . .'], ['T', '_'], ['U', '. . _'], ['V', '. . . _'], ['W', '. _ _'],
    ['X', '_ . . _'], ['Y', '_ . _ _'], ['Z', '_ _ . .']]
    stringMorse = input('Please enter a sentence to be converted to Morse Code: ')
    stringMorse = stringMorse.upper()
    print('You entered the string:', stringMorse)
    print('\nThe Morse Code equivalent is: \n')
    for charString in stringMorse:
        for ch in morseList:
            if ch[0] == charString:
                print(ch[1], end='')
    print()

########## Problem 5, Alphabetic Telephone Number Translator ##########
def alphaNumTranslator():
    print('\n########## Problem 5, Alphabetic Telephone Number Translator ##########\n')
    alphaNum = [['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'], ['8', '8'], ['9', '9'], ['0', '0'],
    ['A', '2'], ['B', '2'], ['C', '2'], ['D', '3'], ['E', '3'], ['F', '3'],
 	['G', '4'], ['H', '4'], ['I', '4'], ['J', '5'], ['K', '5'], ['L', '5'],
    ['M', '6'], ['N', '6'], ['O', '6'], ['P', '7'], ['Q', '7'], ['R', '7'], ['S', '7'],
    ['T', '8'], ['U', '8'], ['V', '8'], ['W', '9'], ['X', '9'], ['Y', '9'], ['Z', '9']]
    telNum = input('Please enter an alphanumeric telephone number in the format, XXX-XXX-XXXX: ')
    telNum = telNum.upper() # .replace('-','')
    print('You entered the number:', telNum)
    print('Numeric translation is: ',end='')
    for ch in telNum:
        if ch == '-':
            print('-',end='')
        else:
            for num in alphaNum:
                if ch == num[0]:
                    print(num[1], end='')
    print('\n\n')
    
main()