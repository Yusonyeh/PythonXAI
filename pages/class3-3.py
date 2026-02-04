# radom模組練習

import random

# random 1 參數
R1 = random.randrange(6)  # 0~5的隨機整數
print("R1:", R1)

# random 2 參數
R2 = random.randrange(1, 11)  # 1~10的整數
print("R2:", R2)

# random 3 參數
R3 = random.randrange(0, 10, 2)  # 0, 2, 4, 6, 8 的整數
print("R3:", R3)

# 統計 randrange 回傳結果
num = 1000
count = [0, 0, 0, 0, 0]  # 用來記錄1~5出現次數的串列
for i in range(num):
    r = random.randrange(1, 6)  # 1~5的整數
    count[r - 1] += 1
for i in range(1, 6):
    print(f"{i} 出現的次數: {count[i-1]}")

print

# rindint 練習
R4 = random.randint(1, 5)  # 1~5的整數
print("R4:", R4)

# rindint 統計回傳結果
num = 1000
count2 = [0, 0, 0, 0, 0]  # 用來記錄1~5出現次數的串列
for i in range(num):
    r = random.randint(1, 5)  # 1~5的整數
    count2[r - 1] += 1
for i in range(1, 6):
    print(f"{i} 出現的次數: {count2[i-1]}")
