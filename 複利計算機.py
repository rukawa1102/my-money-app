import streamlit as st

# 網頁標題
st.title("💰 我的專屬理財 App")
st.subheader("由 Python 與 Vibe Coding 驅動")

# 左側側邊欄：讓你可以自由改參數
st.sidebar.header("調整參數")
本金 = st.sidebar.number_input("起始本金 (元)", value=1000000, step=100000)
年化 = st.sidebar.slider("預期年化報酬率 (%)", 1.0, 20.0, 8.0)
年數 = st.sidebar.slider("投資年數", 1, 40, 10)

# 計算邏輯
結果 = 本金 * (1 + 年化/100)**年數

# 顯示結果
st.write(f"### 經過 {年數} 年後，你的資產將成長至：")
st.header(f"NT$ {int(結果):,}")

# 畫個小圖表
資產變化 = [本金 * (1 + 年化/100)**i for i in range(年數 + 1)]
st.line_chart(資產變化)