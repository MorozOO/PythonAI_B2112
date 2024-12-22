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

sum_of_even = 0
for num in lst:
    if num % 2 == 0:
        sum_of_even += num
print("Sum of even item list: ", sum_of_even)
sum_of_odd = 0
for num in lst:
    if num % 2 != 0:
        sum_of_odd += num
print("Sum of odd item list: ", sum_of_odd)

sum_elements_mult_3 = 0
for i in range(len(lst)):
    if i % 3 == 0:
        sum_elements_mult_3 += lst[i]
print("Sum of elements that are multiples of 3: ", sum_elements_mult_3)

mult_range=1
min_value_list = min(lst)
max_value_list = max(lst)
index_min = lst.index(min_value_list)
index_max = lst.index(max_value_list)
if index_max<index_min:
    index_max,index_min = index_min,index_max
for i in range(index_min,index_max,1):
   mult_range *= lst[i]
print("the product of the elements between the minimum and maximum element: ", mult_range)
