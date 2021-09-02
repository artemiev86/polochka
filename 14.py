# def record(path, header, data, mode='a'):
#     with open(path, mode, encoding='utf-8') as f:
#         f_writer = csv.writer(f, delimiter=';')
#         if os.stat(path).st_size == 0:
#             f_writer.writerow(header)
#         f_writer.writerow(data)


# dic_sums = {}
#         for i, num in enumerate(nums):
#             if num not in dic_sums:
#                 dic_sums[target - num] = i
#             else:
#                 return dic_sums[num], i
import random

# kortez1 = tuple(n for n in range(1, 10))
# kortez2 = tuple(random.randint(1, 10) for x in range(1, 10))
# print(kortez1)
# print(kortez2)
# if sum(kortez1) > sum(kortez2):
#     print(sum(kortez1))
# else:
#     print(sum(kortez2))
# print(kortez1.index(max(kortez1)))
# print(kortez2.index(max(kortez2)))

spis = [1, 2, 3, 4, 2, 1, 2, 3, 4]
print(spis)
spis2 = 0
for i in spis:
    for x in spis[spis.index(i) + 1:]:
        if i == x:
            spis2 += 1
print(spis2)

#
# import random
#
# numbers = [random.randint(1, 2) for i in range(4)]
# print(numbers)
# couples = 0
#
# for number in enumerate(numbers):
#     for i in numbers[number[0]+1:]:
#         if number[1] == i:
#             couples += 1
#
# print(couples)


# nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
#         'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
#         'XC': 90, 'CD': 400, 'CM': 900}
# s = input("введите римские цифры для перевода")
# res = 0
# i = 0
# while i < len(s):
#     if i + 1 < len(s) and s[i] + s[i + 1] in nums:
#         res += nums[s[i] + s[i + 1]]
#         i += 2
#     else:
#         res += nums[s[i]]
#         i += 1
# print(res)
