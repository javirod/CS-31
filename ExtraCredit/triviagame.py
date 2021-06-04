####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Extra Credit Project
# Due Date: 06 JUN 2021
####################################################
import question

def main():
    scorePlayer1 = 0
    scorePlayer2 = 0

    questionList = makeList()

    playerCount = 1
    for item in questionList:
        if playerCount % 2 == 1:
            print('\n~*~*~*~*~*~ Question for Player 1 ~*~*~*~*~*~')
            player = 1
        else:
            print('\n~*~*~*~*~*~ Question for Player 2 ~*~*~*~*~*~')
            player = 2
        
        print(item.__str__())

        selection = int(input('\nPlease make a selection (between 1-4): '))
        while selection < 1 or selection > 4:
            print('Answer not valid.')
            selection = int(input('\nPlease make a selection (between 1-4): '))

        if item.isCorrect(selection) and player == 1:
            print('Congrats you answered correctly!')
            scorePlayer1 += 1
        elif item.isCorrect(selection) and player == 2:
            print('Congrats you answered correctly!')
            scorePlayer2 += 1
        else:
            print('Sorry, your answer was incorrect.')
            print(f'The correct answer is {item.getCorrectAnswer()}')

        playerCount += 1

    print('\n~*~*~*~*~*~ Final Score ~*~*~*~*~*~')
    print(f'Player 1: {scorePlayer1} points')
    print(f'Player 2: {scorePlayer2} points')

    if scorePlayer1 > scorePlayer2:
        print('Player 1 won the game!\n')
    elif scorePlayer2 > scorePlayer1:
        print('Player 2 won the game!\n')
    else:
        print('\nThe game is tied!\n')

def makeList():
    question_list = []
    question_obj1 = question.Question('How many days are in a lunar year?', '354', '365', '243', '379', 1)

    question_obj2 = question.Question('What is the largest planet?', 'Mars', 'Jupiter', 'Earth', 'Saturn', 2)

    question_obj3 = question.Question('What is the largest kind of whale?', 'Orca whale', 'Humpback whale', 'Beluga whale','Blue whale', 4)

    question_obj4 = question.Question('Which dinosaur could fly?', 'Triceratops', 'Tyrannosaurus Rex', 'Pteranodon', 'Diplodocus', 3)

    question_obj5 = question.Question('Which of these Winnie the Pooh characters is a donkey?', 'Pooh', 'Eeyore', 'Piglet', 'Kanga', 2)

    question_obj6 = question.Question('What is the hottest planet?', 'Mars', 'Pluto', 'Earth', 'Venus', 4)

    question_obj7 = question.Question('Which dinosaur had the largest brain compared to body size?', 'Troodon', 'Stegosaurus', 'Ichthyosaurus', 'Gigantoraptor', 1)

    question_obj8 = question.Question('What is the largest type of penguin?', 'Chinstrap penguin', 'Macaroni penguin', 'Emperor penguin', 'White-flippered penguin', 3)

    question_obj9 = question.Question('Which children’s story character is a monkey?', 'Winnie the Pooh', 'Curious George', 'Horton', 'Goofy', 2)
    
    question_obj10 = question.Question('How long is a year on Mars?', '550 Earth days', '498 Earth days', '126 Earth days', '687 Earth days', 4)

    question_list.append(question_obj1)
    question_list.append(question_obj2)
    question_list.append(question_obj3)
    question_list.append(question_obj4)
    question_list.append(question_obj5)
    question_list.append(question_obj6)
    question_list.append(question_obj7)
    question_list.append(question_obj8)
    question_list.append(question_obj9)
    question_list.append(question_obj10)

    return question_list

main()