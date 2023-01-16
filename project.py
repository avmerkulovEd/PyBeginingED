from gametasks import * #printInstructions, getUserScore, updateUserScore
from gameclasses import * #Game, MathGame, BinaryGame

try:
    mathInstructions = 'В этой игре вам предлагается решить простую арифметическую задачу.\nЗа каждый правильный ответ вам начисляется одно очко.\nЗа ошибочные ответы очки не вычитаются.'
    binaryInstructions = 'В этой игре вы получаете десятичное число.\nВаша задача — преобразовать его в двоичную систему cчисления.\nЗа каждый правильный ответ вам начисляется одно очко.\nЗа ошибочные ответы очки не вычитаются.'
    mg = MathGame() #конструируем классы
    bg = BinaryGame() #конструируем классы
    #print('test1')
    userName = input('Введите имя:')
    #print(userName)
    score = int(getUserScore(userName)) #получаем очки из файла
    if score == -1:
        newUser = True
        score = 0
    else:
        newUser = False
    print('Привет %s! Твой счет %s' %(userName, score))

    userChoice = 0
    while userChoice != '-1':
        game = input('1. Math Game\n2. Binary Game\n')
        while game != '1' and game != '2':
            print('Нет такой игры! Повторите выбор')
            game = input('1. Math Game\n2. Binary Game\n')
            
        numPrompt = input('Сколько вопросов 1-10 желаете?')
        while True:
            try:
                num = int(numPrompt)
                if num < 1:
                    num = 1
                if num > 10:
                    num = 10
                break
            except:
                print('Чет не то вводишь')
                numPrompt = input('Сколько вопросов 1-10 желаете?')
                
        if game == '1': #Первая игра
            mg.noOfQuestions = num
            print(mathInstructions)
            score = score + mg.generateQuestions() #Увеличиваем очки
        else: #Вторая игра
            bg.noOfQuestions = num
            print(binaryInstructions)
            score = score + bg.generateQuestions() #Увеличиваем очки

        print('Ваши очки:' + str(score))
        userChoice = input('Enter: Играем дальше\n-1: Выход\n')
        
    updateUserScore(newUser, userName, str(score)) #Обновляем таблицу очков
except Exception as e:
    print('Что-то пошло не так. Game over')
    print("Error: ", e) #Выдать описание ошибки

