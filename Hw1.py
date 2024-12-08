# https://itstepedu-my.sharepoint.com/:u:/g/personal/moroz_oo_itstep_academy/EZnl4-9GS7JKn9NbOfFrxBgBZCm8QYZhd3j7kD_oy0jNxw?e=KDqVdO
#1004

num = float(input("Enter num:"))
integer_num = int(num)
print(round(num))
print(integer_num)
print(f"{(num-integer_num):.1f}")


#1005
x,y = map(int, input().split())
res = x**3+((x+1)/(y**2+1))
print(f"{res:.1f}")


#1006
x,y = map(int, input().split())
print(x - y)