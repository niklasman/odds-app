import streamlit as st
from pathlib import Path

st.set_page_config(page_title="亚盘计算器", layout="wide")

# 隐藏 Streamlit 自带的页头
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# 读取你的 HTML 并显示出来
html_file = Path("index.html")
if html_file.exists():
    st.components.v1.html(html_file.read_text(encoding='utf-8'), height=900, scrolling=True)
else:
    st.error("找不到 index.html")