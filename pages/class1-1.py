# 單行註解
"""
多行註解
"""

n1 = 3  # 整數
f1 = 3.14  # 浮點數
h1 = True  # 布林值
s1 = "hello"  # 字串

print(3)
print(3.14)
print(True)
print("hello")

a = 10
b = 20
print(a + b)  # 加法
print(a - b)  # 減法
print(a * b)  # 乘法
print(a / b)  # 除法
print(a // b)  # 整除
print(a % b)  # 取餘數
print(a**2)  # 次方

print("hello" + "world")  # 字串連接
print("hello" + " " + "world")  # 字串連接(加空格)
print("hello" * 3)  # 字串重複
print("hello" + "world" * 3)  # 字串連結與重複

name = "Yuson"
age = 16
new_str = f"My name is {name}, and I am {age} years old"  # f-string
print(new_str)

print(len(""))  # 0
print(len("hi"))  # 2
print(len("hello"))  # 5

print(type(10))  # int
print(type(3.14))  # float
print(type(True))  # boll
print(type("hello"))  # str

print(int(True))  # 1
print(int(False))  # 0
print(int("1234"))  # 1234

print(float("3.14"))  #  3.14
print(float(10))  # 10.0

print(bool(1))  #  True
print(bool(0))  #  False
print(bool(-2))  #  True
print(bool(""))  #  False
print(bool("hello"))  #  True

print(str(1234))  #  '1234'
print(str(3.14))  # '3.14'
print(str(True))  # 'True'
print(str(False))  # 'False'

# in1 = input("請輸入內容")
# print("你輸入的內容是:" + in1)
# print(type(in1))  # str

in2 = int(input("請輸入一個半徑: "))
area = 3.14 * in2**2
print(f"半徑為 {in2} 的圓面積是 {area}")
