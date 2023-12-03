import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Gulp Dashboard", page_icon=":beer_mug:",
                   layout="wide")

hide_streamlit_style = """
           <style>
          #MainMenu {visibility: hidden;}
           footer {visibility: hidden;}
           </style>
           """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("""
# :beer: Gulp         
         
####  Finding the next beer for you.         
___
This project was made with :heart: and a few :tumbler_glass:
          by [Christian Gentry](https://www.linkedin.com/in/christian-wl-gentry/).                  
         """)
st.write("""Gulp was conceptualized at a crossroads between beginning my initial journey in data analytics and
         trying to implement an easy way for anyone to find good beer. This was compiled and aggregated
         to show the highest-rated beers from the highest-rated styles globally. For those
         who experiement beyond the macro-brewery lagers that dominate the market, find your next
         favorite beer from a style you are leaning towards. 
         
         """)

excel_file = 'https://github.com/chrisbw3/gulp/blob/4771d6b475db17d789bfba2b1dab60794663cf1c/gulp_master.xlsx'

df = pd.read_excel(
    excel_file,
    engine='openpyxl',
    sheet_name='gulp_master',
    usecols='A,B,C,D,E,W',
    nrows=1991,)

df['sub_style'] = df['sub_style'].astype(str).replace("nan", " ")

st.sidebar.header("Style")
main_style = st.sidebar.selectbox(
    "Select the style:",
    options=df["main_style"].unique())

st.sidebar.header("Sub style")
filtered_df = df[df['main_style'] == main_style]
sub_style = st.sidebar.selectbox(
    "Select the sub-style:",
    options=filtered_df['sub_style'].unique().tolist())

st.sidebar.header("ABV")
filtered_df = df[df['sub_style'] == sub_style]
abv = st.sidebar.multiselect(
    "Select the ABV:",
    options=filtered_df['abv'].unique().tolist(),
)

df_selection = df.query(
    "main_style == @main_style & sub_style == @sub_style & abv == @abv"
)
st.dataframe(df_selection)

st.write("Locate the repository [here](https://github.com/chrisbw3/gulp)")
