---
# 🧩 一、什麼是 Streamlit？

👉 Streamlit 是一個可以把 Python 程式變成「網頁小工具」的套件。
例如：輸入數字、按按鈕、顯示結果。

```python
import streamlit as st
```

意思是：把 Streamlit 叫進來用，簡稱為 st。
---

# 🧮 二、數字輸入框 number_input

```python
number = st.number_input("請輸入一個數字", min_value=0, max_value=100, value=50)
```

意思是：

✅ 顯示一個輸入框
✅ 最小 0，最大 100
✅ 預設是 50

顯示輸入的數字：

```python
st.write(f"你輸入的數字是: {number}")
```

📌 小重點：
`f"文字 {變數}"` 可以把變數放進文字裡。

---

# 🧠 三、成績等第判斷（if 判斷式）

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"
```

意思是：

👉 如果分數 ≥ 90 → A
👉 否則如果 ≥ 80 → B
👉 其他 → F

像在玩「如果……那就……」

---

# 🎈 四、按鈕 button

```python
if st.button("click me"):
    st.balloons()
```

意思是：

👉 按下按鈕
👉 出現氣球 🎈

---

# 🔁 五、重複做事情（for 迴圈）

```python
for i in range(5):
    print("hello")
```

意思是：

👉 重複 5 次
👉 每次印出 hello

---

### 印出數字

```python
for i in range(5):
    print(i)
```

結果：

0
1
2
3
4

---

### 有起點與終點

```python
for i in range(2, 6):
```

👉 從 2 到 5

---

### 每次加 2

```python
for i in range(2, 10, 2):
```

👉 2,4,6,8

---

# 🔺 六、數字金字塔

```python
for i in range(1, height + 1):
    st.write(str(i) * i)
```

假如 height = 4

```
1
22
333
4444
```

👉 數字變成文字
👉 乘法代表「重複幾次」

---

# ⭐ 七、星星箭頭金字塔

```python
"*" * 5
```

代表：

```
*****
```

空白：

```python
" " * 3
```

👉 排好位置再組合成圖形

---

# 📦 八、串列（List）

串列像是「盒子裝很多東西」

```python
L = [1, 2, 3]
```

---

### 各種串列

```python
[1,2,3]           # 數字
["apple","banana"]# 文字
[1,"a",True]      # 混合
```

---

### 取出資料

```python
L = [10,20,30]
print(L[0])   # 10
```

⚠️ 從 0 開始算！

---

### 串列裡還有串列

```python
L = [1,2,[3,4]]
print(L[2][0])  # 3
```

---

# ✂️ 九、切片（挑部分）

```python
L = [1,2,3,"a","b","c"]
L[1:4]
```

結果：

```
[2,3,"a"]
```

---

# 📏 十、長度 len()

```python
len([1,2,3])
```

結果：3

---

# 🔍 十一、走訪串列

### 方法一

```python
for i in range(len(L)):
    print(L[i])
```

### 方法二（比較簡單）

```python
for x in L:
    print(x)
```

---

# ✏️ 十二、修改串列內容

```python
a = [1,2,3]
a[0] = 10
```

變成：

```
[10,2,3]
```

---

### 同一個串列

```python
b = a
```

a 和 b 其實是同一個盒子！

---

# ➕ 十三、串列常用指令

### 加資料

```python
append(4)
```

### 刪第一個符合的

```python
remove(1)
```

### 刪最後一個

```python
pop()
```

### 排序

```python
sort()
```

---

# 📂 十四、讀取檔案

```python
with open("檔名","r",encoding="utf-8") as file:
    content = file.read()
```

👉 開檔案
👉 讀內容

---

# 📄 十五、檔名檢查

```python
file.endswith(".md")
```

👉 判斷是不是 markdown 檔

---

# 📁 十六、取得資料夾內檔案

```python
os.listdir("資料夾")
```

👉 拿到全部檔名清單

---

# 🧱 十七、Streamlit 排版（columns）

```python
col1, col2 = st.columns(2)
```

👉 分成兩欄

---

# ⌨️ 十八、文字輸入框

```python
text = st.text_input("請輸入文字")
```

---

# 🧠 十九、Session State（記住資料）

```python
ss = st.session_state
```

如果沒有 ans：

```python
ss.ans = 0
```

按按鈕就 +1：

```python
ss.ans += 1
```

👉 可以記住數字，不會因為重新整理而消失

---

---

## ✅ 今日重點總整理

✔ Streamlit 可以做網頁介面
✔ if 判斷式做選擇
✔ for 迴圈做重複
✔ 串列用來存很多資料
✔ append / remove / pop / sort 很重要
✔ session_state 可以記住數值

---
