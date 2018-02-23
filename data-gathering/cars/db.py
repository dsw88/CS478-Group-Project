import psycopg2
import os
import json

page_size = 20
db_user = os.environ.get('CARS_DB_USER')
db_pass = os.environ.get('CARS_DB_PASS')
if not db_user or not db_pass:
    raise RuntimeError('You must specify the CARS_DB_USER and CARS_DB_PASS environment variables')
cached_conn = psycopg2.connect("dbname=scraped_cars user={} password={}".format(db_user, db_pass))


def save_listing_details(listing_id, ld):
    print("  Saving details to db")
    cursor = cached_conn.cursor()
    cursor.execute("UPDATE car SET vin = %s, price = %s, fuel_type = %s, mpg_city = %s, mpg_highway = %s, exterior_color = %s, interior_color = %s, engine = %s, mileage = %s, advanced_details = %s WHERE listing_id = %s",
                   (ld.get('vin'), ld.get('price'), ld.get('fuel_type'), ld.get('mpg_city'), ld.get('mpg_highway'), ld.get('exterior_color'), ld.get('interior_color'), ld.get('engine'), ld.get('mileage'), json.dumps(ld['advanced_details']), listing_id))
    cached_conn.commit()
    cursor.close()


def get_listings_to_load(page_num):
    cursor = cached_conn.cursor()
    offset = (page_num - 1) * page_size
    cursor.execute("SELECT listing_id FROM car WHERE vin IS NULL ORDER BY listing_id DESC OFFSET %s LIMIT %s", (offset, page_size))
    results = cursor.fetchall()
    return list(map(lambda row: row[0], results))


def insert_listing_id(listing_id):
    cursor = cached_conn.cursor()
    cursor.execute("SELECT * FROM car WHERE listing_id = %s", (listing_id,))
    result = cursor.fetchone()
    if not result: # Doesn't exist yet, insert it
        print("{} - Inserting into database".format(listing_id))
        cursor.execute("INSERT INTO car (listing_id) VALUES (%s)", (listing_id,))
    else:
        print("{} - Already exists in database".format(listing_id))
    cached_conn.commit()
    cursor.close()
