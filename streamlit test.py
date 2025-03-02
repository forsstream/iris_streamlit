import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

#タイトルとテキストを記入
st.title("Streamlit 基礎")
st.write("Hello World!")

# データフレームの準備
df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})

# 動的なテーブル
st.dataframe(df)
st.dataframe(df.style.highlight_max(axis=0), width=100, height=150)

# 静的テーブル
st.table(df)

# 10 行 3 列のデータフレームを準備
df = pd.DataFrame(
    np.random.rand(10,3),
    columns = ['a', 'b', 'c']
)

# 折れ線グラフ
st.line_chart(df)
#面グラフ
st.area_chart(df)
#棒グラフ
st.bar_chart(df)

# プロットする乱数をデータフレームで用意
df = pd.DataFrame(

    # 乱数 + 新宿の緯度と経度
    np.random.rand(100,2) / [50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)

#マップをプロット
st.map(df)

# 画像の読み込み
img = Image.open("C:\\Python_env\\py3.8env\\streamlit\\Iris.jpg")
st.image(img, caption="アイリス", use_column_width = True)

#チェックボックス
if st.checkbox("show image"):
    img = Image.open("C:\\Python_env\\py3.8env\\streamlit\\Iris.jpg")
    st.image(img, caption="アイリス", use_column_width = True)
    
# セレクトボックス
option = st.selectbox(
    '好きな数字を入力してください。',
    list(range(1, 11))
)

'あなたの好きな数字は' , option , 'です。'

# テキスト入力による値の動的変更
text = st.text_input('あなたの好きなスポーツを教えて下さい。')

'あなたの好きなスポーツ：' , text

# スライダーによる値の動的変更
condition = st.slider('あなたの今の調子は？', 0, 100, 50)

'コンディション：' , condition