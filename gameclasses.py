class Game:

    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions
        
        @property
        def noOfQuestions(self):
            return self._noOfQuestions
        
        @noOfQuestions.setter
        def noOfQuestions(self, value):
            if value < 1:
                self._noOfQuestion = 1
                print('Минимальное количество вопросов = 1')
                print('Так-что будет задан один вопрос')
            elif value > 10:
                self._noOfQuestion = 10
                print('Максимальное количество вопросов = 10')
                print('Так-что будет задано десять вопросов')
            else:
                self._noOfQuestion = value

class BinaryGame(Game):

    def generateQuestions(self):
        from random import randint
        
        score = 0
        for i in range(self.noOfQuestions):
             base10 = randint(1, 100)
             print(base10)
             userResult = input('Введите ответ в двоичном коде')
             while True:
                 try:
                     answer = int(userResult, base = 2)
                     if answer == base10:
                         print('Молодец! +100 очков Гриффиндору')
                         score += 100
                         break
                     else:
                         print('Неправильно! Ответ: ' + bin(base10))
                         break
                 except:
                     print('Неправильно. Вводи снова.')
                     userResult = input()
        return(score)                     

class MathGame(Game):

    def generateQuestions(self):
        from random import randint
        
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = [' ', ' ', ' ', ' ', '']
        operatorDict = {0: '+', 1: '-', 2: '*', 3: '**'}
        questionString = ''
        
        for i in range(self.noOfQuestions):
            for j in range(5):
                numberList[j] = randint(1, 9)
            for j in range(4):    
                ran_dom = randint(0, 3)
                if (ran_dom != 3) or ('**' not in symbolList):
                    symbolList[j] = operatorDict[ran_dom]
            for j in range(5):
                questionString = questionString + str(numberList[j]) + symbolList[j]
            result = eval(questionString)
            questionString = questionString.replace("**", "^")
            print('Вычислите выражение: ' + questionString)
            userResult = input()
             
            while True:
                try:
                    answer = int(userResult)
                    if answer == result:
                        print('Молодец! +100 очков Гриффиндору')
                        score += 100
                        questionString = ''
                        break
                    else:
                        print('Неправильно! Ответ: ' + str(result))
                        questionString = ''
                        break
                except:
                    print('Неправильно. Вводи снова.')
                    userResult = input()
        return(score)
