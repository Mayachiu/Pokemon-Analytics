import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#from plotly.offline import plot as plt

st.title("ポケモンのデータ分析アプリ")

"ポケモンのデータ"
pokemon = pd.read_csv("http://logopt.com/data/poke.csv",encoding="utf-8")
st.dataframe(pokemon,width=1000)

select_list=["HP","Attack","Defense","Sp. Atk","Sp. Def","Speed","Generation","Legendary"]
select_list2=["Legendary","Generation"]
option = st.sidebar.selectbox(
    "x軸に表示するデータを選んでください",
    select_list
)

"x軸は",option,"です"

option2 = st.sidebar.selectbox(
    "y軸に表示するデータを選んでください",
    select_list
)

"y軸は",option2,"です"

if st.sidebar.checkbox("colorを追加する"):
    color_select=st.sidebar.selectbox("データを選んで下さい",select_list)
    "colorは",color_select,"です"
else:
    color_select=None


if st.sidebar.checkbox("sizeを追加する"):
    size_select=st.sidebar.selectbox("データを選んで下さい",select_list,key="add_size")
    "sizeは",size_select,"です"
else:
    size_select=None


if st.sidebar.checkbox("facet_rowを追加する"):
    facet_row_select=st.sidebar.selectbox("データを選んで下さい",select_list2,key="add_facet_row")
    "facet_rowは",facet_row_select,"です"
else:
    facet_row_select=None



st.write(px.scatter(pokemon,x =option,y = option2,color=color_select,facet_row=facet_row_select,hover_name="Japanese",size=size_select))



text = st.text_input('考察', '考察を入力してください')



