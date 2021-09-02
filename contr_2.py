# C_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# C_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# if sum(C_1) > sum(C_2):
#     print("сумма  больше в кортеже", C_1)
# elif sum(C_1) == sum(C_2):
#     print("сумма чисел кортежа равна")
# else:
#     print("сумма  больше в кортеже", C_2)
# print(C_1.index(min(C_1)), C_1.index(max(C_1)))
# print(C_2.index(min(C_1)), C_1.index(max(C_2)))

# stroka = "An apple a day keeps the doctor away"
# strok = ''.join(stroka.split())
# slovar = {i: strok.count(i) for i in strok}
# print(slovar)

# spis_1 = [1, 3, 2, 4, 6, 3]
# spis_2 = [2, 1, 3, 4, 5, 2]
# set_spis_1 = set(spis_1)
# set_spis_2 = set(spis_2)
# print(len(set_spis_1 & set_spis_2))

# try:
#     x = 2 / 0
# except ZeroDivisionError:
#     print("нельзя делить на 0")
# finally:
#     print("если даже возникнет ошибка я выполню этот принт")
# или вариант с ошибкой
# try:
#     x = 2 / 0
# finally:
#     print("если даже возникнет ошибка я выполню этот принт")


# a = [1, 2, 3, 3, 5, 6, 4, 1, 3]
# x = []
# for i in a:
#     if a.count(i) == 1:
#         x.append(i)
# print(*x)


# spisok = [1, 2, 1, 1]         # тут есть вопрос!!!
# par = 0
# for spis in enumerate(spisok):
#     for i in spisok[spis[0] + 1:]:
#         if spisok[1] == i:
#             par += 1
# print(par)


# file_klass = open("jurnal .txt", "r", encoding="utf-8")
# n = 0
# for i in file_klass:
#     i = i.split(" ")
#     if int(i[2]) < 3:
#         print(i[1], i[2])
#     n = n+int(i[2])
# print(n / 3)

# torti = [["снежок", "бисквитный", 20, 5], ["свитанок", "медовый", 15, 10],
#          ["банан", "йогуртный", 13, 4]]
# print(torti[0][0], torti[1][0], torti[2][0])
# vopros = input("что вас интересует: описание, цена, количество тортиков? или вся информация")
# tor = torti[0][0]
# if vopros == "описание":
#     print(torti[0][0], torti[0][1], torti[1][0], torti[1][1], torti[2][0], torti[2][1], )
# elif vopros == "цена":
#         print(torti[0][0], torti[0][2], torti[1][0], torti[1][2], torti[2][0], torti[2][2], )
# elif vopros == "количество":
#     print(torti[0][0], torti[0][3], torti[1][0], torti[1][3], torti[2][0], torti[2][3], )
# else:
#     print()