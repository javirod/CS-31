
####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Extra Credit Project
# Due Date: 06 JUN 2021
####################################################
class Question:
    def __init__(self, quest, ans1, ans2, ans3, ans4, correctAns):
        self.__question = quest
        self.__answer1 = ans1
        self.__answer2 = ans2
        self.__answer3 = ans3
        self.__answer4 = ans4
        self.__correctAnswer = correctAns

    # set methods
    def setQuestion(self, quest):
        self.__question = quest
    def setAnswer1(self, ans1):
        self.__answer1 = ans1   
    def setAnswer2(self, ans2):
        self.__answer2 = ans2   
    def setAnswer3(self, ans3):
        self.__answer3 = ans3   
    def setAnswer4(self, ans4):
        self.__answer4 = ans4   
    def setCorrectAnswer(self, correctAns):
        self.__correctAnswer = correctAns   

    # get methods
    def getQuestion(self):
        return self.__question
    def getAnswer1(self):
        return self.__answer1
    def getAnswer2(self):
        return self.__answer2
    def getAnswer3(self):
        return self.__answer3
    def getAnswer4(self):
        return self.__answer4
    def getCorrectAnswer(self):
        return self.__correctAnswer
    
    def __str__(self):
        return self.__question + '\n1.  ' + self.__answer1 + '\n2.  ' + self.__answer2 +\
        '\n3.  ' + self.__answer3 + '\n4.  ' + self.__answer4
    
    def isCorrect(self, selAnsw):
        if selAnsw == self.__correctAnswer:
            return True
        else:
            return False