import streamlit as st
from pathlib import Path

# 1. 设置页面配置，去掉多余的侧边栏，使用宽屏模式
st.set_page_config(page_title="亚盘计算器", layout="wide", initial_sidebar_state="collapsed")

# 2. 隐藏 Streamlit 默认的顶部菜单栏和底部水印（让它看起来像一个纯粹的网页）
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {padding-top: 1rem; padding-bottom: 0rem;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. 读取同目录下的 V5.html 并嵌入（注意这里的文件名是 V5.html）
html_file = Path("V5.html")

if html_file.exists():
    # 读取 HTML 内容并渲染，高度设大一点防止出现双重滚动条
    st.components.v1.html(html_file.read_text(encoding='utf-8'), height=950, scrolling=True)
else:
    st.error("找不到 V5.html 文件，请检查文件名或路径！")