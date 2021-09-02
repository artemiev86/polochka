import csv
import os

import random


# fio = 'миша'
# mail = 'nikolai@mail.ru'
# pfone = '+375295495325'
# with open('user.csv', 'a', encoding='utf - 8') as f:
#     f_writer = csv.writer(f, delimiter=';')
#     if os.stat('user.csv').st_size == 0:
#         f_writer.writerow(['id', 'ФИО', "Почта", 'Телефон'])
#     id = random.randint(1000, 10000)
#     f_writer.writerow([id, fio, mail, pfone])


# fio = 'марина'
# mail = 'nikolai@mail.ru'
# pfone = '+375295495325'
# with open('user.csv', 'r', encoding='utf-8') as f:
#     f_reader = csv.DictReader(f, delimiter=';')
#     for line in f_reader:
#         if 'коля' in line['ФИО']:
#             print(line)


# def record(path, header, data, mode='a'):
#     with open(path, mode, encoding='utf-8') as f:
#         f_writer = csv.writer(f, delimiter=';')
#         if os.stat(path).st_size == 0:
#             f_writer.writerow(header)
#         f_writer.writerow(data)

# def vse_dannie(path):
#     with open(path, 'r', encoding='utf-8') as f:
#         f_reader = csv.reader(f, delimiter=';')
#         for line in f_reader:
#             print(line)
# vse_dannie('user.csv')

# def reed2(path, key):
#     with open(path, 'r', encoding='utf-8') as f:
#         f_reader = csv.reader(f, delimiter=';')
#         for line in f_reader:
#             if key in line:
#                 print(line)
#
#
# reed2('user.csv', 'миша', )

def obnov_csv(path, fio):
    with open(path, 'r', encoding='utf-8') as f:
        f_reader = csv.reader(f, delimiter=';')
