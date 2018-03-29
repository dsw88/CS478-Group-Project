I performed some initial cleaning in the CSV such as stripping off whitespace and extra quotes around the data columns. 

I then loaded it up in the Jupyter notebook in this directory and ran the pandas-profiling tool on it.

# Data Analysis Phase 1
The following issues are in the data:
* Way too many colors: 1083. This is the same problem as the Cars.com dataset
* 2 cars had null make values. This seems like a crucial feature, so I deleted those 2 rows.
* Lots of people put the incorrect mileages on their cars to get them to show up in searches. For example "150", which really usually means "150,000" miles.
    * I deleted 35 rows with fewer than 400 miles that were older than 2017
* There are lots of new cars masquerading as used cars in this dataset. I did a spot check on new cars with fewer than 100 miles, and they were all new cars for sale. Since this is a used car prediction, I deleted 7,892 cars with fewer than 100 miles, which are likely new cars for sale.
* 1833 cars had null mileage. This seems like another crucial feature,  and I don't know that we can reliably impute values since they vary so much from car to car, even in the same year. I deleted them from the database.
* I deleted 31 cars with a mileage > 350,000. Many of these cars had an absurdly high value that couldn't be real.
* I accidentally deleted 700 cars with a bad query...
* I deleted cars with > $150,000 price
* I deleted cars from year < 1990, same as for Cars.com dataset