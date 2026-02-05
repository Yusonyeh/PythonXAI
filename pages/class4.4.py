# 全域變數與區域變數

from calendar import c


Length = 5  # 全域變數


def calculate_square_area():
    area = Length * Length  # 區域變數
    print("面積為：", area)


calculate_square_area()

print("-" * 30)

length = 5  # 全域變數


def calculate_square_area2():
    area = length * length  # 區域變數
    print("面積為：", area)


length = 10  # 全域變數
calculate_square_area2()

# print("-" * 30)

# Length = 5  # 全域變數


# def calculate_square_area3():
#     area = Length * Length  # 區域變數


# length = 10  # 全域變數
# calculate_square_area3()
# print("面積為：", area)

print("-" * 30)

Length = 5  # 全域變數
area = 3.14 * 10**2  # 區域變數


def calculate_circle_area4():
    area = Length * Length  # 區域變數


def calculate_circle_area4():
    area = Length * Length  # 區域變數


calculate_square_area()
print("面積為：", area)

print("-" * 30)

length = 5  # 全域變數
area = 3.14 * 10**2  # 區域變數


def calculate_square_area7():
    global area
    area = length * length  # 區域變數


calculate_square_area7()
print("面積為：", area)
