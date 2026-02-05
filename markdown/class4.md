---

# 🖼 一、Streamlit：顯示圖片

### ✅ 匯入需要的工具

```python
import streamlit as st
import os
```

👉 就像請幫手來幫我們做網頁與找檔案。

---

### ✅ 顯示標題

```python
st.title("圖片元件")
```

👉 在網頁上顯示大標題。

---

### ✅ 顯示一張圖片

```python
st.image("image/wenby.png", width=300, caption="WENBY")
```

意思是：

- 顯示圖片
- 寬度 300
- 圖片下面顯示文字說明

---

### ✅ 讀取資料夾內所有圖片

```python
image_folder = "image"
image_files = os.listdir(image_folder)
image_files.sort()
```

👉 把 image 資料夾裡的檔案名稱全部抓出來。

---

### ✅ 用迴圈顯示所有圖片

```python
for image_file in image_files:
    st.image(image_folder + "/" + image_file)
```

👉 一張一張顯示。

---

### ✅ 圖片自動填滿寬度

```python
st.image(image_path, use_container_width=True)
```

---

# 🔽 二、下拉選單（選圖片）

```python
selected_image = st.selectbox("選擇圖片", image_files)
```

👉 讓使用者用下拉選單選圖片。

```python
st.image(image_folder + "/" + selected_image)
```

👉 顯示選到的圖片。

---

# 💬 三、訊息提示元件

四種訊息：

```python
st.success("成功")
st.error("錯誤")
st.warning("警告")
st.info("資訊")
```

---

### ✅ 按下按鈕顯示訊息

```python
if st.button("success按鈕"):
    st.success("成功")
```

---

### ✅ 重新整理畫面

```python
st.rerun()
```

👉 重新執行整個程式。

---

# 🛒 四、購物平台（簡單版）

---

### ✅ session_state

```python
ss = st.session_state
```

👉 用來「記住資料」，不會因為刷新就消失。

---

### ✅ 建立商品資料

每個商品有：

```
圖片
價格
庫存
```

像這樣：

```python
ss.product["apple"] = {
   "image_path": "...",
   "price": 10,
   "stock": 10
}
```

---

### ✅ 顯示商品

```python
st.image(...)
st.write(商品名稱)
st.write(價格)
st.write(庫存)
```

---

### ✅ 購買按鈕

```python
if details["stock"] > 0:
    details["stock"] -= 1
```

👉 庫存大於 0 才能買。

---

### ✅ 新增庫存

```python
ss.product[商品]["stock"] += 數量
```

---

### ✅ 顯示目前庫存

```python
for name, details in ss.product.items():
    st.write(name, details["stock"])
```

---

# 🧩 五、函數（Function）

### ✅ 最簡單函數

```python
def hello():
    print("hello")
```

使用：

```python
hello()
```

👉 每呼叫一次就印 hello。

---

### ✅ 有參數的函數

```python
def greet(name):
    print("hello", name)
```

```python
greet("Alice")
```

---

### ✅ 回傳結果的函數

```python
def two_num_min(a, b):
    if a < b:
        return a
    else:
        return b
```

👉 找出比較小的數字。

---

### ✅ 三個數字比大小

```python
def three_num_min(a, b, c):
```

👉 回傳三個數中最小的。

---

### ✅ 預設參數

```python
def calculate_circle_area(radius, pi=3.14):
```

如果沒有給 pi → 自動用 3.14。

---

### ✅ 指定參數名稱

```python
print_parameters(1, 2, d=4)
```

👉 可以只指定想改的。

---

# 🌍 六、全域變數 & 區域變數

### ✅ 全域變數

在函數外面：

```python
length = 5
```

### ✅ 區域變數

在函數裡：

```python
area = length * length
```

只能在函數裡用。

---

### ❌ 函數外不能用裡面的變數

會出錯。

---

### ✅ global（讓函數改外面的變數）

```python
global area
area = length * length
```

👉 告訴 Python：我要用外面的 area。

---

# ⭐ 重點總整理

✔ st.image() 顯示圖片
✔ for 迴圈可重複做事情
✔ selectbox 可選資料
✔ session_state 記住資料
✔ def 建立函數
✔ return 回傳結果
✔ 變數有「裡面」與「外面」的差別

---
