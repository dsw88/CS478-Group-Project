# Data Preprocessing Session 1
The data that comes back from Cars in my scraping script isn't all equally useful. Some of it isn't totally clean:
* The model field is sometimes missing
* The model field is sometimes an aggregation of year, make, model, and trim.

I did the following preprocessing steps on the cars dataset:
* Remove cars with a year < 1990. Of the 47,087 cars, only 204 were from prior to 1990. Many of these were collectors items that were worth a lot, which I thought might have confused the algorithm with respect to year, making it seem like both the newest and oldest cars were the most valuable, while that is only true for a subset of old cars.
* Of the remaining rows, some of them had bad model names where they contained the year, make, model, and trim in the model field. 
* Of these bad model names, 4,520 only had 2 or fewer cars in the dataset for that model. I deleted these cars with bad model names < 2 because they needed manual fixing and I can't reasonably do that much data cleaning in a single semester. In a longer project we would have tried to salvage these.
* After the previous step, it left 42,363.
* Some car brands have the trim in their model name. Example: BMW 3-series has the 330, 335, etc., but they are all fundamentally the same model with differing levels of trim.
    * BMW
    * Lexus

# Initial Analysis
I used the pandas-profiling library, which is very helpful for analyzing the data set. The following issues came up:
* Exterior color has high cardinality: 2513 colors, all of them cool-sounding variations on the 10-20 common colors. (e.g. "Artic Metalic" instead of "Silver")
* Model still has a high cardinality: 495 values
* Miles per gallon city is highly correlated with miles per gallon highway (of course, should have thought of that sooner)
* State has 52 values, need to investigate there...should only have 50 max
* Transmission has high cardinality: 768. There really should only be 3 or so.
* Trim has so many values missing that there's no point in including it. 75.9% values missing.
* Need to delete the "New" cars, there are 4 of them. I'm not sure how they got in.
* Some of the mileages are outrageously high, they have to be mistakes. I might want to remove any higher than 300,000 miles
* listingid and vin are of course extremely high cardinality, I'm leaving those in the CSV but they will not be features.
* Need to analyze Make to ensure there are no duplicates, but it's looking pretty good.
* Miles per gallon (city) is a good feature to use
* Get rid of number of doors feature
* Get rid of excessively expensive cars, since these are outliers. Probably cap it at no more than 150,000 or 200,000.
* 

# Data Preprocessing Session 2
* Did some color reduction, I only have about 2,000 rows left that are still odd manufacturer colors
* Deleted cars that were > $150,000
* Put all transmission types into "Manual", "Automatic", or missing
* Deleted the "New" cars.
* Deleted all cars with mileages over 310,000 miles. There weren't many, and they were obvious mistakes. I wasn't sure what to impute there.

# Analysis #2
* 52 states is correct, it's including Puerto Rico and D.C.
* Color needs lots more work, still 473 distinct values
* Model needs more looking at?
* It's hard to decide which models to combine. 3-series was obvious, but it's harder for things like the Volvo S90 and S60, because they are two very different levels of cars

# Data Preprocessing Session 3
* Did more work with colors
* 