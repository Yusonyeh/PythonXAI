import streamlit as st

st.title("課堂筆記")

with st.expander("Class 1"):
    st.write(
        ''''
        📘 1-1 基本資料與運算

一、基本資料種類

n1 = 3        # 整數
f1 = 3.14     # 小數
h1 = True     # 是或否
s1 = "hello"  # 文字

--------------------
二、顯示東西

print(3)
print(3.14)
print(True)
print("hello")

print = 把東西顯示出來

--------------------
三、變數與數學運算

a = 10
b = 20

print(a + b)   # 加
print(a - b)   # 減
print(a * b)   # 乘
print(a / b)   # 除
print(a // b)  # 整除
print(a % b)   # 餘數
print(a**2)    # 次方

--------------------
四、文字運算

print("hello" + "world")
print("hello" + " " + "world")
print("hello" * 3)
print("hello" + "world" * 3)

+ 代表接起來
* 代表重複

--------------------
五、把變數放進句子

name = "Yuson"
age = 16
print(f"My name is {name}, and I am {age} years old")

--------------------
六、看文字長度

print(len(""))
print(len("hi"))
print(len("hello"))

len = 有幾個字

--------------------
七、看資料種類

print(type(10))
print(type(3.14))
print(type(True))
print(type("hello"))

--------------------
八、資料轉換

轉成整數:
int(True)
int(False)
int("1234")

轉成小數:
float("3.14")
float(10)

轉成是或否:
bool(1)
bool(0)
bool("")
bool("hello")

轉成文字:
str(1234)
str(3.14)
str(True)

--------------------
九、使用者輸入

in1 = input("請輸入內容:")

輸入的資料都是文字

--------------------
十、算圓面積

r = int(input("請輸入一個半徑: "))
area = 3.14 * r * r
print(f"半徑為 {r} 的圓面積是 {area}")

--------------------
🎯 重點記住

print = 顯示  
input = 輸入  
+ - * / = 數學運算  
文字要加 " "

📗 1-2 Streamlit 基本顯示

--------------------
一、匯入 Streamlit

import streamlit as st

--------------------
二、設定標題

st.title("class1-2")

--------------------
三、顯示文字 (write)

st.write("Hello")

--------------------
四、Markdown 語法顯示

st.write(
"""
# H1        最大標題
## H2
### H3
#### H4
##### H5
###### H6

* **粗體**
* *斜體*
* [連結](https://www.google.com)

程式碼顯示方式:

```python
print("Hello, World!")

📙 1-3 比較、邏輯、條件判斷

--------------------
一、比較運算子（比大小）

print(1 == 1)   # 等於
print(1 != 1)   # 不等於
print(2 > 1)    # 大於
print(2 < 1)    # 小於
print(2 >= 2)   # 大於等於
print(2 <= 1)   # 小於等於

--------------------
二、not（相反）

print(not True)    # False
print(not False)   # True

--------------------
三、and（而且）

print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

全部都 True → 才是 True

--------------------
四、or（或）

print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

有一個 True → 就是 True

--------------------
五、if 判斷（如果）

password = input("請輸入密碼:")

if password == "1234":
    print("歡迎，yuson")

--------------------
六、if else（如果...不然）

if password == "1234":
    print("歡迎，yuson")
else:
    print("密碼錯誤")

--------------------
七、if elif else（多種情況）

if password == "1234":
    print("歡迎，yuson")
elif password == "0000":
    print("歡迎，max")
else:
    print("密碼錯誤")

--------------------
🎯 重點記住

== 是比較  
= 是設定值  
if 後面要加 :  
裡面的程式要縮排（往右空4格）

        '''
    )
