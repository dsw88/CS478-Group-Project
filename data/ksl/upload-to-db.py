import csv
import os
import psycopg2
import uuid

db_user = os.environ.get('CARS_DB_USER')
db_pass = os.environ.get('CARS_DB_PASS')
if not db_user or not db_pass:
    raise RuntimeError('You must specify the CARS_DB_USER and CARS_DB_PASS environment variables')
cached_conn = psycopg2.connect("dbname=scraped_cars user={} password={}".format(db_user, db_pass))

with open('scraped_data/ksl-scraped.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        listing_id = str(uuid.uuid4())  # listing_id (KSL didn't have one like Cars, so we just make this up)
        vin = row[0].strip() if row[0].strip() != '' else None  # vin
        print("Loading car {} into the database".format(vin))
        year = row[1].strip() if row[1].strip() != '' else None  # year
        model = row[2].strip() if row[2].strip() != '' else None  # model
        make = row[3].strip() if row[3].strip() != '' else None  # make
        transmission = row[4].strip() if row[4].strip() != '' else None  # transmission
        exterior_color = row[5].strip() if row[5].strip() != '' else None  # exterior_color
        state = row[6].strip() if row[6].strip() != '' else None  # state
        mileage = row[7].strip() if row[7].strip() != '' else None  # mileage
        price = row[8].strip() if row[8].strip() != '' else None  # price

        cursor = cached_conn.cursor()
        sql = """
            INSERT INTO car (
              listing_id,
              vin,
              year,
              model,
              make,
              transmission,
              exterior_color,
              state,
              mileage,
              price,
              source
            )
            VALUES (
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
            """
        params = (
            listing_id,
            vin,
            year,
            model,
            make,
            transmission,
            exterior_color,
            state,
            mileage,
            price,
            "KSL.com"
        )
        cursor.execute(sql, params)
        cached_conn.commit()
        cursor.close()
