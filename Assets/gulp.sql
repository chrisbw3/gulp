-----------------------------------------
--Created the table in PostgreSQL server.
create table public."BeerProfileAndReviews"
("Name" varchar (250), main_style varchar (100), sub_style varchar (100), Brewery varchar (250),	
 ABV NUMERIC (5), MinIBU INT, MaxIBU INT , Astringency INT,
 Body INT, Alcohol INT,	Bitter INT, Sweet INT,
 Sour INT, Salty INT, Fruits INT, Hoppy INT, Spices INT,
 Malty INT, ReviewAroma decimal (9,3), ReviewAppearance decimal (9,3), 
 ReviewPalate decimal (9,3), ReviewTaste decimal (9,3), 
 ReviewOverall decimal (9,3), NumberOfReviews NUMERIC (10));

--Loaded the csv file into SQL server.

COPY public."BeerProfileAndReviews" FROM '/private/tmp/beer_profile_and_ratings.csv'
DELIMITER ',' csv header ;

--The initial query to determine the popularity of the top 10 styles of beer.

SELECT "main_style",
AVG(reviewoverall) AS reviewoverall_avg
FROM public."BeerProfileAndReviews"
WHERE numberofreviews>=500
GROUP BY "main_style"
ORDER BY reviewoverall_avg DESC
LIMIT 10;

--Query for all beers in each style as long as they have 50 reviews to avoid uncommon beers.

SELECT *
from public."BeerProfileAndReviews"
WHERE numberofreviews>=50
AND main_style='RedAle'
limit 10

--Find the average rating overall's relationship to abv.

SELECT abv, AVG(reviewoverall) AS rev_avg
FROM public."BeerProfileAndReviews"
GROUP BY abv
ORDER BY rev_avg DESC;

--Query the 10 worst beer styles in the database, still avoiding uncommon beers.
SELECT "main_style",
AVG(reviewoverall) AS reviewoverall_avg
FROM public."BeerProfileAndReviews"
WHERE numberofreviews>=500
GROUP BY "main_style"
ORDER BY reviewoverall_avg ASC
LIMIT 10;




 
 