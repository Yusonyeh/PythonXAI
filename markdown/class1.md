# 📝 Python 基礎筆記

## 1️⃣ 註解

```python
# 這是單行註解
"""
這是
多行註解
"""
```

---

## 2️⃣ 變數 & 資料型態

- **整數**：3, 10, -5 → `int`
- **浮點數**：3.14, 10.0 → `float`
- **布林值**：True / False → `bool`
- **字串**：文字，放在 "" 或 '' → `str`

```python
n1 = 3
f1 = 3.14
h1 = True
s1 = "hello"
```

- 可以用 `print()` 看結果：

```python
print(3)
print(3.14)
print(True)
print("hello")
```

---

## 3️⃣ 數字運算

```python
a = 10
b = 20
print(a + b)  # 加法  30
print(a - b)  # 減法  -10
print(a * b)  # 乘法  200
print(a / b)  # 除法  0.5
print(a // b) # 整除  0
print(a % b)  # 取餘數 10
print(a**2)   # 次方  100
```

---

## 4️⃣ 字串操作

```python
print("hello" + "world")        # 合併字串 → "helloworld"
print("hello" + " " + "world")  # 加空格 → "hello world"
print("hello" * 3)               # 重複字串 → "hellohellohello"
```

### f-string（方便把變數放進字串）

```python
name = "Yuson"
age = 16
print(f"My name is {name}, and I am {age} years old")
```

---

## 5️⃣ 字串長度 & 型態

```python
print(len("hello"))       # 5
print(type(10))           # int
print(type(3.14))         # float
print(type(True))         # bool
print(type("hello"))      # str
```

---

## 6️⃣ 型態轉換

```python
int(True)      # 1
int(False)     # 0
float("3.14")  # 3.14
bool(0)        # False
bool("hello")  # True
str(123)       # "123"
```

---

## 7️⃣ 使用者輸入

```python
# input() 都會得到字串
in1 = input("請輸入內容: ")
print("你輸入的是：" + in1)

# 如果要算數字，要轉型
in2 = int(input("請輸入半徑: "))
area = 3.14 * in2**2
print(f"半徑為 {in2} 的圓面積是 {area}")
```

---

## 8️⃣ 比較運算

- `==` 等於
- `!=` 不等於
- `>` 大於
- `<` 小於
- `>=` 大於等於
- `<=` 小於等於

```python
print(1 == 1)  # True
print(2 > 1)   # True
print(2 < 1)   # False
```

---

## 9️⃣ 邏輯運算

- `not` 取反
- `and` 兩個都對才對
- `or` 有一個對就對

```python
print(not True)       # False
print(True and False) # False
print(True or False)  # True
```

---

## 🔟 條件判斷

```python
password = input("請輸入密碼: ")

if password == "1234":
    print("歡迎，yuson")
elif password == "0000":
    print("歡迎，max")
else:
    print("密碼錯誤，請重新輸入")
```

- `if`：如果…
- `elif`：如果前面都不對，再看這個條件
- `else`：其他情況

---

## 1️⃣1️⃣ Streamlit（簡單寫網頁）

````python
import streamlit as st

st.title("class1-2")
st.write("""
# H1
## H2
### H3
* **粗體**
* *斜體*
* [連結](https://www.google.com)
```python
print("Hello, World!")
````

""")

```

- `st.title()` 顯示標題
- `st.write()` 顯示文字或程式碼

---
```
