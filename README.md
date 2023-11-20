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
## Importing, Querying, Analyzing in SQL
Created the table in PostgreSQL server.
```
create table public."BeerProfileAndReviews"
("Name" varchar (250), main_style varchar (100), sub_style varchar (100), Brewery varchar (250),	
 ABV NUMERIC (5), MinIBU INT, MaxIBU INT , Astringency INT,
 Body INT, Alcohol INT,	Bitter INT, Sweet INT,
 Sour INT, Salty INT, Fruits INT, Hoppy INT, Spices INT,
 Malty INT, ReviewAroma decimal (9,3), ReviewAppearance decimal (9,3), 
 ReviewPalate decimal (9,3), ReviewTaste decimal (9,3), 
 ReviewOverall decimal (9,3), NumberOfReviews NUMERIC (10));
```
Loaded the csv file into SQL server.
```
COPY public."BeerProfileAndReviews" FROM '/private/tmp/beer_profile_and_ratings.csv'
DELIMITER ',' csv header ;
```
The initial query to determine how many different main styles
```
select "main_style",
AVG(reviewoverall) as reviewoverall_avg
from public."BeerProfileAndReviews"
where numberofreviews>=500
GROUP BY "main_style"
ORDER BY reviewoverall_avg desc
LIMIT 50;
```
