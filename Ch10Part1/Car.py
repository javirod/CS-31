# Week 16, ICAs 1 and 2
class Car:
    def __init__(self, yr, mk, md):
        self.__year = yr
        self.__make = mk
        self.__model = md
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 10

    def brake(self):
        self.__speed -= 10
    
    def how_fast(self):
        return self.__speed
    
    def __str__(self) -> str:
        return 'Your ' + self.__year + ' ' + self.__make + ' ' + self.__model + ' is going ' + str(self.__speed) + ' MPH.'
