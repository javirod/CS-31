class Employee:
    def __init__(self, n, id, d, t):
        self.__name = n
        self.__id = id
        self.__dept = d
        self.__title = t   
    # set methods
    def setName(self, n):
        self.__name = n   
    def setID(self, id):
        self.__id = id    
    def setDept(self,d):
        self.__dept = d   
    def setTitle(self, t):
        self.__title = t    
    # get methods
    def getName(self):
        return self.__name   
    def getID(self):
        return self.__id
    def getDept(self):
        return self.__dept
    def getTitle(self):
        return self.__title
    def __str__(self):
        return 'Name: '+ self.__name + ' ID: ' + self.__id +\
        ' Dept: '+ self.__dept + ' Title: ' + self.__title