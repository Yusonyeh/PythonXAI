# 算術指定運算子

a = 10
b = 3
a += b  # a = a + b
print("a+=b:", a)

a = 10
b = 3
a -= b  # a = a - b
print("a-=b的結果:", a)

a = 10
b = 3
a *= b  # a = a * b
print("a*=b的結果:", a)

a = 10
b = 3
a /= b  # a = a / b
print("a/=b的結果:", a)

a = 10
b = 3
a //= b  # a = a // b
print("a//=b的結果:", a)

a = 10
b = 3
a %= b  # a = a % b
print("a%=b的結果:", a)

a = 10
b = 3
a **= b  # a = a ** b
print("a**=b的結果:", a)

print("-" * 30)

# while 迴圈練習
i = 0
while i < 5:
    print("i=", i)
    i += 1

print("-" * 30)

# while 迴圈break
i = 1
while i <= 6:
    if i == 3:
        break
    print("1=", i)
    i += 1

print("-" * 30)

# for 迴圈 break
for i in range(1, 6):
    if i == 3:
        break
    print("i=", i)
