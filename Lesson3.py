# https://itstepedu-my.sharepoint.com/:u:/g/personal/moroz_oo_itstep_academy/EU-MaXNmUu5BldGntYpBYEYBv8bj7ZnH0-6V7TbBCqlw9w?e=jhIyeo
#1015

# seconds = int(input())
# print(seconds//60)

# 1016
# a,b = map(int, input().split())
# print(a - (a // b) * b)

#1017

# x = int(input())
# if x % 2 == 0:
#     print("Yes")
# else:
#     print("No")

#1018
# a,b = map(int, input().split())
# if a > b:
#     print(a*2)
# else:
#     print(b*2)

#1019
# a = int(input())
# if a % 2 == 0:
#     print(int(a / 2))
# else:
#     print(0)


#1020
# a,b = map(int, input().split())
# if b>a:
#     print(a,b)
# else:
#     print(b,a)

#1021
# p = float(input())
# if p % 1 == 0: print("Yes")
# else: print("No")

#1021
a,b,c,d = map(int, input().split())
min,max = 0,0
if a>d and a>c and a>d:
    max = a
elif b>a and b>c and b>d:
    max = b
elif c>a and c>b and c>d:
    max = c
else: max = d

if a<d and a<c and a<d:
    min = a
elif b<a and b<c and b<d:
    min = b
elif c<a and c<b and c<d:
    min = c
else: min = d

print(min,max)