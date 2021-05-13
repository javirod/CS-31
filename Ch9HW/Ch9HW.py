####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Chapter 9 Homework
# Due Date: 16 MAY 2021
####################################################

def main():
    courseInfo()
    uniquewords()
    fileAnalysis()

########## Problem 1, Course Information ##########
def courseInfo():
    print('\n########## Problem 1, Course Information ##########\n')
    courseRoom = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755', 'NT110':'1244', 'CM241':'1411'}
    courseInstructor = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
    courseTime = {'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.', 'CS103':'10:00 a.m.', 'NT110':'11:00 a.m.', 'CM241':'1:00 p.m.'}

    repeat = 'y'
    while repeat == 'y' or repeat == 'Y':
        course = input('Please enter a course to display info: ')
        if course in courseRoom:
            print(f'\n{course:10}Room Number: {courseRoom[course]:10}Instructor: {courseInstructor[course]:10}Time: {courseTime[course]:10}')
        else:
            print('Course does not exist.')
        print()
        repeat = input('Would you like the course info for another class? (y/n): ')


########## Problem 4, Unique Words ##########
def uniquewords():
    print('\n########## Problem 4, Unique Words ##########')
    print('Note: All words have been converted to lower case, so words are not repeated due to case\n')
    infile = open('words1.txt', 'r')
    words1 = infile.read().lower()
    infile.close()
    listWords1 = words1.split()
    setWords1 = set(listWords1)
    print('Unique words in the words1.txt:')
    print('-------------------------------')
    print(setWords1)
    print()


########## Problem 6, File Analysis ##########
def fileAnalysis():
    print('\n########## Problem 6, File Analysis ##########')
    print('Note: All words have been converted to lower case, so words are not repeated due to case\n')
    infile1 = open('words1.txt', 'r')
    infile2 = open('words2.txt', 'r')
    words1 = infile1.read().lower()
    words2 = infile2.read().lower()
    infile1.close()
    infile2.close()
    listWords1 = words1.split()
    listWords2 = words2.split()
    setWords1 = set(listWords1)
    setWords2 = set(listWords2)
    # It should display a list of all the unique words contained in both files.
    print('\nUnion - unique words contained in both files:')
    print('---------------------------------------------')
    unionWords = setWords1 | setWords2 # setWords1.union(setWords2)
    print(unionWords)
    # It should display a list of the words that appear in both files.
    print('\nIntersection - words that appear in both files:')
    print('-----------------------------------------------')
    intersectionWords = setWords1 & setWords2 # setWords1.intersection(setWords2)
    print(intersectionWords)
    # It should display a list of the words that appear in the first file but not the second.
    print('\nDifference - words that appear in the first file but not the second:')
    print('--------------------------------------------------------------------')
    diff1 = setWords1 - setWords2
    print(diff1)
    # It should display a list of the words that appear in the second file but not the first.
    print('\nDifference - words that appear in the second file but not the first:')
    print('--------------------------------------------------------------------')
    diff2 = setWords2 - setWords1
    print(diff2)
    # It should display a list of the words that appear in either the first or second file, but not both.
    print('\nSymmetric Difference - words that appear in either the first or second file, but not both:')
    print('------------------------------------------------------------------------------------------')
    symmDiff = setWords1 ^ setWords2
    print(symmDiff)
    print()

main()