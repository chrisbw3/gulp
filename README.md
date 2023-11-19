# Gulp: Finding What Beers Does the World Enjoy?
### Overview
This project started as a personal interest to find the highest-rated beers worldwide. The goal was to analyze what beers are the highest rated regarding several attributes, such as: style, abv, and reviews based on a 1-5 scale system. Finally, an interactive dashboard was created for users to find recommendations for what beer they should shop for next.
### Data Sources
The data was retrieved from the [Kaggle dataset here](https://www.kaggle.com/datasets/ruthgn/beer-profile-and-ratings-data-set?rvi=1).
### Tools Used
- Excel - Cleaning
- PostgreSQL - Analysis
- Tableau - Reporting

### Data Cleaning & Preparation
Cleaning and preparing the data involved:
1. Loading and inspecting the data.
2. Looking for any missing values/bad data.
3. Creating appropriate formatting and  adding columns.
### Visualization
Results were visualized using Tableau.

## Cleaning & Preparing 
After loading the Beer_Profile_And_Ratings.csv into Excel, some initial adjustments were made.

The “style” column often contained extensions to the names that would be more suited for “sub_styles”. To quickly achieve this, two and new columns were inserted and the following formulas were used:

Only include the first, "main" style in first new column.
```
=IFERROR(LEFT($B2,FIND(“-“,$B2)-1), "")
```
Only include the secondary, "sub" style in second new column.
```
=IFERROR(REPLACE($B2,1,FIND("-",$B2),””), "")
```
