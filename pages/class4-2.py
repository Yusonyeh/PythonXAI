import select
import streamlit as st
import os
import time

ss = st.session_state

image_folder = "image"
image_files = os.listdir(image_folder)
image_files.sort()

if "product" not in ss:
    ss.product = {}
    for image_file in image_files:
        product_name = image_file[:-4]
        ss.product[product_name] = {
            "image_path": image_folder + "/" + image_file,
            "price": 10,
            "stock": 10,
        }

st.title("購物平台")

col1Num = st.number_input("請輸入商品數量", min_value=1, max_value=5, value=3, step=1)
cols = st.columns(col1Num)
counter = 0

for name, details in ss.product.items():
    with cols[counter % col1Num]:
        st.image(details["image_path"])
        st.write(f"## {name}")
        st.write(f"### 價格: ${details['price']}")
        st.write(f"### 庫存: {details['stock']}")
        if st.button(f"購買 {name}"):
            if details["stock"] > 0:
                details["stock"] -= 1
                st.success(f"成功購買 {name}")
            else:
                st.error(f"(name)庫存不足")
            time.sleep(1)
            st.rerun()
    counter += 1

st.title("新增商品庫存")

col1, col2 = st.columns(2)
selected_product = col1.selectbox("選擇商品", ss.product.keys())
add_stock = col2.number_input("請輸入庫存數量", min_value=0, value=1, step=1)
if st.button("新增庫存"):
    ss.product[selected_product]["stock"] += add_stock
    st.success(f"(selected_product)庫存已新增 {add_stock} 個")
    time.sleep(1)
    st.rerun()

st.title("目前庫存")
for name, details in ss.product.items():
    st.write(f"## {name}: {details['stock']}件")
