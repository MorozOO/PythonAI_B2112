# import math
# from random import randint
#
# # print(lst)
# # lst.append(math.pi)
# # lst.append(math.e)
# # print(lst)
# # lst.clear()
# # print(lst)
# lst = []
# size = int(input())
# for i in range(size):
#     lst.append(randint(-10, 10))
# print(lst)
#
# print(lst[3])
#
# lst2 = [randint(-10,10) for i in range(10)]
# print(lst2)
#
# lstNum = [i for i in range(10)]
# print(lstNum)
#
# lst_even = [i for i in range(10) if i % 2 == 0]
# print(lst_even)
#
# lst_odd = [i for i in range(10) if i % 2 != 0]
# print(lst_odd)
#
# lst_mult_square = [i**2 for i in range(10)]
# print(lst_mult_square)
#
# for i in lst_mult_square:
#     print(i)

from random import randint

lst = [randint(-10, 10) for i in range(20)]
print(lst)

sum_negative = 0

for num in lst:
    if num < 0: sum_negative += num
print("Sum negative item list: ", sum_negative)
