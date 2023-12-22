import pandas as pd
import folium
import openpyxl
import streamlit as st
from streamlit_folium import folium_static

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

excel_file = 'https://github.com/chrisbw3/gulp/blob/d26297ae3b321bbbbe19391012ee55462f883532/gulp_master.xlsx'

df = pd.read_excel(
    excel_file,
    engine='openpyxl',
    sheet_name='gulp_master',
    usecols='A,B,C,D,F,G,H,Z',
    nrows=1991,)

latitude_col='latitude'
longitude_col='longitude'

df = df.dropna(subset=[latitude_col, longitude_col])

df['sub_style'] = df['sub_style'].astype(str).replace("nan", "")

st.sidebar.header("Style")
main_style = st.sidebar.selectbox(
    "Select the style:",
    options=df["main_style"].unique()
    )

st.sidebar.header("Sub style")
filtered_df = df[df['main_style'] == main_style]
sub_style = st.sidebar.selectbox(
    "Select the sub-style:",
    options=filtered_df['sub_style'].unique().tolist()
   )

st.sidebar.header("ABV")
filtered_df = df[df['sub_style'] == sub_style]
abv = st.sidebar.multiselect(
    "Select the ABV:",
    options=filtered_df['abv'].unique().tolist()
)

df_selection = df.query(
    "main_style == @main_style & sub_style == @sub_style & abv == @abv"
)


st.dataframe(df_selection)

map_center = [df_selection[latitude_col].mean(), df_selection[longitude_col].mean()]
my_map = folium.Map(location=map_center, zoom_start=5)

for index, row in df_selection.iterrows():
    folium.Marker([row[latitude_col], row[longitude_col]], popup=row['brewery']).add_to(my_map)

folium_static(my_map, width=1100, height=500)


st.write("Locate the repository [here](https://github.com/chrisbw3/gulp)")
