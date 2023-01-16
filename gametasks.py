def printInstructions(instruction):
    print(instruction)

'''функция для считывания очков или создания файла очков''' 
def getUserScore(userName): 
    try:    
        f = open('userScores.txt', 'r')
        for line in f:
            resolt = line.split(', ')
            content = {resolt[0]: resolt[1]}
            #print(content)
            if str(userName) in content:
                f.close()
                return(resolt[1])
        f.close()
        return('-1')
    except IOError:
        print('Файл не найден. Создаю новый')
        f = open('userScores.txt', 'w')
        f.close()
        return('-1')

'''функция для записи очков старых игроков и добавления новых игроков'''
def updateUserScore(newUser, userName, score):
    from os import remove, rename
    
    if newUser == True:
        f = open('userScores.txt', 'a')
        f.write(userName + ', ' + score + '\n')
        f.close()
    else:
        t = open('userScores.tmp', 'w')#открываем временный файл
        f = open('userScores.txt', 'r')#открываем старый файл
        for line in f:
            resolt = line.split(', ')
            content = {resolt[0]: resolt[1]}
            if userName in content:
                t.write(userName + ', ' + score + '\n')
            else:
                t.write(line)
        t.close()
        f.close()
        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')
