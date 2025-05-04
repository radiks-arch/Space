from random import choice
from time import sleep


def guess_the_word():
    word = ["тунель", "лошадь", "удачка", "листок", "ворона", "гитара"]
    return choice(word)


def rules_of_the_game(otvet):
    while True:
        if otvet.lower() in ["да", "lf"]:
            return """
                Программа придумывает слово из шести букв. 
                Игрок должен отгадать слово и не повеситься. 
                Нужно называть одну букву и если она есть в слове(ед.ч.), то она ставится на свое место.
                Если игрок ошибся, то программа добавляет часть тела на виселицу. =)
                """
        if otvet.lower() in ["нет", "ytn"]:
            return choice(["Отлично!", "Ну тогда вперед!", "Удачи!"])
        sleep(1)
        otvet = input("Некорректный ввод! Введите -да, -нет: ")
        sleep(1)


def guessed_right(char_user):
    index = 0
    for char in guess:
        if char == char_user:
            del correct_guess[index]
            correct_guess.insert(index, char)
        index += 1
    print(*correct_guess)


def wrong(count):
    if count == 1:
        sleep(1)
        print("Добовляю голову")
        sleep(1)
        print(
            """
            _____
            |   &
            |   O
            |     
            |
            |       """
        )
        sleep(1)
    elif count == 2:
        sleep(1)
        print("Добовляю туловище")
        sleep(1)
        print(
            """
            _____
            |   &
            |   O
            |   | 
            |
            |       """
        )
        sleep(1)
    elif count == 3:
        sleep(1)
        print("Добовляю руку")
        sleep(1)
        print(
            """
            _____
            |   &
            |   O
            |  /| 
            |       
            |       """
        )
        sleep(1)
    elif count == 4:
        sleep(1)
        print("Добовляю вторую руку")
        sleep(1)
        print(
            """
            _____
            |   &
            |   O 
            |  /|\ 
            |    
            |       """
        )
        sleep(1)
    elif count == 5:
        sleep(1)
        print("Добовляю ногу")
        sleep(1)
        print(
            """
            _____
            |   &
            |   O 
            |  /|\ 
            |  /  
            |       """
        )
        sleep(1)
    elif count == 6:
        sleep(1)
        print("Добовляю вторую ногу")
        sleep(1)
        print(
            """
            _____
            |   &
            |   O 
            |  /|\ 
            |  / \ 
            |       """
        )
        sleep(1)


def clue():
    global repeated_letters
    clue_guess = []
    for char in guess:
        clue_guess.append(char)
    char_user = choice(clue_guess)
    index = 0
    for char in guess:
        if char == char_user:
            del correct_guess[index]
            correct_guess.insert(index, char)
        index += 1
    repeated_letters.append(char_user)
    repeated_letters.append("`")
    repeated_letters.append("~")
    repeated_letters.append("Ё")
    repeated_letters.append("ё")
    print(*correct_guess)


def game(char_user):
    count = 0
    while True:
        repeated = True
        if char_user in repeated_letters:
            sleep(1)
            print(f"Вы уже использовали!: {char_user}")
            sleep(1)
            repeated = False
        if char_user.lower() in ["ё", "`"] and repeated == True:
            clue()
            repeated = False
        if char_user.lower() in guess and repeated == True:
            guessed_right(char_user)
        if char_user.lower() not in guess and repeated == True:
            count += 1
            wrong(count)
            if count == 6:
                return False
        if "".join(correct_guess) == guess:
            return True
        repeated_letters.append(char_user)
        sleep(1)
        char_user = input("Вводите букву(подсказка на клавишу ё): ")
        sleep(1)


def again(otvet):
    while True:
        if otvet.lower() in ["да", "lf"]:
            return True
        if otvet.lower() in ["нет", "ytn"]:
            return False
        sleep(1)
        otvet = input("Некорректный ввод! Введите -да, -нет: ")
        sleep(1)


enter = input('Добро подаловать на веселую игру "ВИСЕЛИЦА"!')


while True:
    guess = guess_the_word()
    correct_guess = ["_"] * 6
    repeated_letters = []
    sleep(1)
    print(rules_of_the_game(input("Нужно ли вам объяснить правила? -да, -нет: ")))
    sleep(1)
    win = game(
        input(
            "Я загадал слово. Введите предположительную букву в слове на русском(подсказка на букву ё): "
        )
    )
    if win:
        sleep(1)
        print(f"Поздравляю ты выиграл! Я загадал слово: {guess}")
        sleep(1)
    else:
        sleep(1)
        print("О нет, ты повесился. =(")
        sleep(1)
        print(f"Я загадал слолво: {guess}")
        sleep(1)
    again_otvet = again(input("Желаете ли вы продолжить? -да, -нет: "))
    if again_otvet:
        continue
    else:
        sleep(1)
        print(choice(["До скорой встречи!", "Пока!", "Еще увидимся!"]))
        sleep(1)
        break
