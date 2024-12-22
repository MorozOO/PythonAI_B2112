print("HW2")
# 1023
x,y = map(int, input().split())
if x < 0 and y > 0:
    print("Yes")
else:
    print("No")

#1027
num = int(input())
a = num //1000
b = num //100 % 10
c = num //10 % 10
d = num % 10
# if a > b and a > c and a > d: print(a)
# elif b > a and b > c and b > d: print(b)
# elif c > a and c > b and c > d: print(c)
# else : print(d)
print(max(a,b,c,d))


# 1025

x, y, z = map(int, input().split())
if x + y > z and y + z > x and z + x > y:
    print("Yes")
else:
    print("No")