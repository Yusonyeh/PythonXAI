import random


def roll_dice(n):
    for i in range(n):
        number = random.randint(1, 6)
        print("第", i + 1, "次擲到：", number)


# 讓使用者輸入次數
times = int(input("請輸入要擲骰子的次數："))
roll_dice(times)
