# Регистрацию
# 1) ФИО
# 2) Телефон Проверка: +375 и количество чисел
# 3) Почту Проверка на собачку и точку после
import random

# words = ["hi-4", "my", "name"] words[0]
# for word in enumerate(words): word = [0, "hi"], word = [1, "my"], word = [
#     word[0] = 0,1,2
#     word[1]= hi-4,my,name
# for word in words: word = "hi", word = "my"

print("Вас приветствует Альфа-банк")
FIO = input("введите своё ФИО: ")
while True:
    PHONE = input("введите, пожалуйста, свой телефон: ")
    if PHONE[:4] == "+375" and len(PHONE) == 13 and PHONE[1:].isdigit():
        break
    print("Введите корректные значения")
while True:
    MAIL = input("введите, пожалуйста вашу электронную почту: ")
    if '@' in MAIL:
        if '.' in MAIL[MAIL.index("@"):]:
            break
    print("Введите корректные значения")
NUMBERS = []
MONEY = []
CVV = []
STATUS = []
HISTORY = []
while True:
    print(
        "Меню:\n1 - Добавить карту\n2- Перевод на карту или счёт\n3 - принять перевод\n4 - Платежи\n5 - Заблокировать карту")
    print("6 - Вывести все карты\n7 - посмотреть историю карты\n0 - Выйти ")
    choice = input("Ваш выбор: ")
    if choice == "1":
        while True:
            number = input("Введите номер новой карты: ")
            if len(number) == 16 and number.isdigit():
                break
            print("Введите корректные значения")
        NUMBERS.append(number)
        MONEY.append(0)
        while True:
            cvv = random.randint(100, 999)
            if cvv not in CVV:
                CVV.append(cvv)
                break
        STATUS.append("Разблокирована")
    elif choice == "2":
        if NUMBERS:
            print("Номер\t\t\t Деньги\t CVV\t Статус")
            for number in enumerate(NUMBERS):
                print(number[0]+1, number[1], str(MONEY[number[0]]) + " $\t", CVV[number[0]], STATUS[number[0]])
            print("С какой карты вы бы хотели сделать перевод: ")
            number = int(input("Ваш выбор: "))
            if abs(number) > len(NUMBERS):
                print("Нет такой карты")
            else:
                number_receiver = input("Введите номер карточки получателя: ")
                money = input("Введите количество денег, которые будут переведены: ")
                if number_receiver in NUMBERS:
                    MONEY[NUMBERS.index(number_receiver)] += int(money)
                    HISTORY.append([number_receiver, "Получен перевод на " + str(money)])
                MONEY[number-1] -= int(money)
                HISTORY.append([NUMBERS[number-1], "Сделан перевод на "+str(money)])
        else:
            print("у вас пока нет карточек")
    elif choice == "3":
        if NUMBERS:
            print("Номер\t\t\t Деньги\t CVV\t Статус")
            for number in enumerate(NUMBERS):
                print(number[0]+1, number[1], str(MONEY[number[0]]) + " $\t", CVV[number[0]], STATUS[number[0]])
            print("На какую карту вы бы хотели получить перевод? ")
            number = int(input("Ваш выбор: "))
            money = int(input("Сколько денег вы хотите получить: "))
            HISTORY.append([NUMBERS[number-1], "Получен перевод на "+str(money)])
            MONEY[number-1] += money
        else:
            print("У вас пока нет карточек")
    elif choice == "5":
        if NUMBERS:
            print("Номер\t\t\t Деньги\t CVV\t Статус")
            for number in enumerate(NUMBERS):
                print(number[1], str(MONEY[number[0]])+" $\t", CVV[number[0]], STATUS[number[0]])
            number = int(input("какуб карточку вы хотите заблокировать/разблокировать: "))
            if STATUS[number-1] == "Разблокирована":
                STATUS[number-1] = "Заблокирована"
            else:
                STATUS[number-1] = "Разблокирована"
        else:
            print("У вас пока нет карточек")
    elif choice == "6":
        if NUMBERS:
            print("Номер\t\t\t Деньги\t CVV\t Статус")
            for number in enumerate(NUMBERS):
                print(number[1], str(MONEY[number[0]])+" $\t", CVV[number[0]], STATUS[number[0]])
        else:
            print("У вас пока нет карточек")
    elif choice == "7":
        if NUMBERS:
            print("Номер\t\t\t Деньги\t CVV\t Статус")
            for number in enumerate(NUMBERS):
                print(number[0] + 1, number[1], str(MONEY[number[0]]) + " $\t", CVV[number[0]], STATUS[number[0]])
            print("Историю какой карты вы бы хотели получить выписку: ")
            number = int(input("Ваш выбор: "))
            for story in HISTORY:
                if story[0] == NUMBERS[number-1]:
                    print(story)
        else:
            print("у вас пока не карточек")
    elif choice == "0":
        print("До свидания")
        break
    else:
        print("Неправильный ввод")