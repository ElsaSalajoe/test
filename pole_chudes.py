import random
words = ["любовь", "катастрофа", "гесперида", "инфотехнологии", "Иггдрасиль", "катарсис"]
word = random.choice(words)
tries = len(word) 
letter = 0
word2 = ""
name = input("Введите своё имя: ")
print("Здраствуйте,", name + "!")
print('Добро пожаловать на игру "Поле чудес!"')
print("Условия игры простые: вам надо угадать слово, загаданное нами.")
print("Вам даётся на это " + str(tries) + " попыток.")
print("Удачи!")
userInput = input("Вы согласны? Для продолжения нажмите Enter: ")
print("Отлично! Игра началась!")
print("В этом слове", tries, "букв")
s = tries * ("* ").split()
print("Теперь вы можете", tries,"раз спросить меня, есть ли какая-то буква в этом слове.\n")
for _ in word:
    letter = input("Назовите следующую букву: ")
    if letter in word:
        position = word.find(letter)
        print(position)
        print(letter)
        s[position] = letter
        print(s)
        print(word2)
        #print(s.replace("*", letter, 1))
        print("Вы угадали! Откройте букву", letter, "!")
    else:
        print("В этом слеве нет такой буквы")
        print(s)
answer = input("Какое слово было загадано?\n")
if answer == word:

    print("И перед нами победитель сегодняшней игры! \nПоздравляем вас!")
    n = 6
    for row in range(0,n):
        for col in range(0,n+1):
            if(row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
                print("*",end=" ")
            else:
                print(" ",end=" ")              
        print()
if answer != word:
    print(word)
    print("Очень жаль, вы проиграили!")
    print("Приходите снова, может быть, в следующий раз вам больше повезёт!")







"""





import random

dictionary = ("CROWS", "GOAT", "MONKEY", "COW", "HORSE", "SNAKE")
answer = random.choice(dictionary)
answer_length = len(answer)
victory = True
print("I have chosen a word.  Your job is to guess it. I will help you keep track.")

print("The word I have chosen is {} letters long.\n".format(answer_length))

underscores = []
for character in answer:
    underscores.append("_")
print(underscores)

while victory:
    guess = input("\nPlease guess a letter: ").strip().capitalize()
    def pos(guess):
        position = 0
        for letter in answer:
            if letter != guess:
                position += 1
            else:
                print("Correct!")
                break
        return position

    def update_board(x):
        global underscores
        if guess in answer:
            underscores[x] = guess
        else:
            print("This letter is not in the word")
        return underscores

    def winner():
        global underscores
        global victory
        if "_" not in underscores:
            print("YOU HAVE WON!")
            victory = False

    x = pos(guess)
    print(update_board(x))
    winner()


"""

