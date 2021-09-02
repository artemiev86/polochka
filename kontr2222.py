# spis = open('slovarik.txt', 'r', encoding='utf - 8')  # задача 1
# for i in spis:
#     i = i.split(',')
# spis.close()
# spis1 = i[0]
# i.pop(0)
# print({spis1: dict(zip(i[::2], i[1::2]))})

# obnov = open('obnovlenie.txt', 'r', encoding='utf - 8')  # задача 2
# for i in obnov:
#     i = i.split(',')
#     print(i)
# obnov.close()
# x = int(input("введите индекс элемента для корректировки"))
# i[x] = input("введите измененный элемент ")
# print(i)
# obnov = open('obnovlenie.txt', 'w', encoding='utf - 8')
# obnov.write(','.join(i))
# obnov.close()

# nums = [1, 3, 6, 9, 8, 2, 1, 45]
# target = 325
# nums.sort()
# nums.reverse()
# print(nums)
# indexi = []
# while True:
#     for i in nums:
#         if target % i > 0 and not target // i == 0:
#             n = target // i
#             indexi.append(n * str(nums.index(i)))
#             target = target - n * i
#             print(indexi)


# nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
#         'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
#         'XC': 90, 'CD': 400, 'CM': 900}
# s = input("введите римские цифры для перевода")
# rez = 0
# i = 0
# while i < len(s):
#     if i + 1 < len(s) and s[i] + s[i + 1] in nums:
#         rez += nums[s[i] + s[i + 1]]
#         i += 1
#     else:
#         rez += nums[s[i]]
#         i += 1
# print(rez)


