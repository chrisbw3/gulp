# Gulp: Finding What Beers Does the World Enjoy? :beers:

## 🎉v2.0 is here🎉
With API use and adding geospacial visualization, read more about the newest update below.

### Overview
This project started as a personal interest to find the highest-rated beers worldwide. The goal was to analyze what beers are the highest rated regarding several attributes, such as: style, abv, and reviews based on a 1-5 scale system. Finally, an interactive dashboard was created for users to find recommendations for what beer they should shop for next.
### Data Sources 📊
The data was retrieved from the [Kaggle dataset here](https://www.kaggle.com/datasets/ruthgn/beer-profile-and-ratings-data-set?rvi=1).
### Tools Used 🛠️
- #### Excel - Cleaning
- #### PostgreSQL - Analysis
- #### Tableau - Graph Visualization
- #### Python
  - Streamlit
  - Pandas
  - Plotly

### Data Cleaning & Preparation 🧼
Cleaning and preparing the data involved:
1. Loading and inspecting the data.
2. Looking for any missing values/bad data.
3. Creating appropriate formatting and  adding columns.
### Visualization 🖼️
Results were visualized using Tableau.

## What Questions Need Answered? :thought_balloon:
 - What styles of beer are most popular?
 - Do consumers enjoy higher abv compared to lower abv?
 - What style beers should you avoid buying?

## Key Findings 🔍
### Predominately European style beers were most well-received. 🇪🇺
This may not come as a surprise, given Europe's history with the alcoholic beverage is naturally older than the West. These are styles not commonly seen from the macro-breweries like Anheuser Busch or Coors.

![](https://github.com/chrisbw3/gulp/blob/a1d9e1c1c0ebc0a4f9425be64f3aa0f068207ea1/Assets/top_10_styles.png)

### There was a correlation between higher ABV and higher reviews. 📈
This is logical as most of the top 10 styles are historically brewed at higher ABV percentages.

<img src="https://github.com/chrisbw3/gulp/blob/a1d9e1c1c0ebc0a4f9425be64f3aa0f068207ea1/Assets/abv_by_rating.png" width="1100" height="500"/>

### What kinds of beer should be avoided? ❌
The answer to this is, frankly, none of them. While looking at the top 10 worst-rated beers, even the worst still received an average 3.4/5 rating. While there's certainly room for improvement, no notable styles have an average rating below this modest figure.

![](https://github.com/chrisbw3/gulp/blob/b4b457e528d6ef6b2bc29cb542d3b88d5a086ad1/Assets/10_worst_beers.png)



## Cleaning & Preparing 🧼
After loading the Beer_Profile_And_Ratings.csv into Excel, some initial adjustments were made.

The “style” column often contained extensions to the names that would be more suited for “sub_styles”. To quickly achieve this, two new columns were inserted. To make the process of separating the "style" into main and sub styles quickly over hundreds of rows, the following formulas were used:

Only include the first, "main" style in first new column.
```
=IFERROR(LEFT($B2,FIND(“-“,$B2)-1), "$B2")
```
Only include the secondary, "sub" style in second new column.
```
=IFERROR(REPLACE($B2,1,FIND("-",$B2),””), "")
```
![Adding Columns](https://github.com/chrisbw3/gulp/blob/6232cec802f05d054e300df700b22ff12513b448/Assets/adding_columns.png)

The original style column was removed after copy/pasting as values for the new main and sub style columns.
## Importing, Querying, Analyzing in SQL 🕵️
For all SQL queries, refer to ["gulp.sql" in the Assets folder](https://github.com/chrisbw3/gulp/blob/e93efa8d3092b3180f315741942809852f300f73/Assets/gulp.sql).

## Launching the Web Application 🚀
Gulp was conceptualized at a crossroads between beginning my initial journey in data analytics and trying to implement an easy way for anyone to find good beer. After concluding my findings earlier, I realized that I was left with nearly 2,000 notable beers I had never tried or heard of. Using streamlit and other Python libraries, an easy to use web app was created with the purpose of giving quick recommendations to those looking for their next favorite beer.
![](https://github.com/chrisbw3/gulp/blob/779ecec9a76355c63dd9c8637dfd6581c8910e4d/Assets/GIF%20Recording%202023-12-02%20at%2011.51.34%20PM.gif)

### Access the web application [here](https://gulpapp.streamlit.app).

## v2 📣
A dynamic Folium map was added to provide geospatial vizualization to help aid the user as a reference for what may be local to their area, and to simply establish an index of where the breweries are located at.

#### Google Geocode API
Google's Geocode API was implemented to first assign ZIP codes for each brewery name. After establishing the ZIP codes, coordinates were established with the API based on the ZIP codes. See [get_adress](https://github.com/chrisbw3/gulp/blob/bcd62782c599ed6d08599c05c4d23b3122d577ff/get_address2.py) and [get_coordinates](https://github.com/chrisbw3/gulp/blob/bcd62782c599ed6d08599c05c4d23b3122d577ff/reverse_geocode.py).
After obtaining the coordinates, the dataset was updated and the folium map was created.

![](https://github.com/chrisbw3/gulp/blob/bcd62782c599ed6d08599c05c4d23b3122d577ff/Assets/map_screenshot.jpeg)
