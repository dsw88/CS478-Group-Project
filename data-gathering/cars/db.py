import psycopg2
import os
import json

page_size = 20
db_user = os.environ.get('CARS_DB_USER')
db_pass = os.environ.get('CARS_DB_PASS')
if not db_user or not db_pass:
    raise RuntimeError('You must specify the CARS_DB_USER and CARS_DB_PASS environment variables')
cached_conn = psycopg2.connect("dbname=scraped_cars user={} password={}".format(db_user, db_pass))


def save_listing_details(listing_id, listing_details):
    print("  Saving details to db")
    cursor = cached_conn.cursor()
    advanced_details = json.dumps(listing_details['advanced_details']) if listing_details.get('advanced_details') else None
    sql = """
    UPDATE car SET 
      vin = %s,
      make = %s,
      model = %s,
      year = %s,
      condition = %s,
      mpg_city = %s,
      mpg_highway = %s,
      fuel_type = %s,
      mileage = %s,
      number_of_doors = %s,
      engine = %s,
      interior_color = %s,
      transmission = %s,
      cars_rating = %s,
      exterior_color = %s,
      city = %s,
      state = %s,
      zip_code = %s,
      advanced_details = %s,
      price = %s
    WHERE listing_id = %s
    """
    params = (
        listing_details.get('vin'),
        listing_details.get('make'),
        listing_details.get('model'),
        listing_details.get('year'),
        listing_details.get('condition'),
        listing_details.get('mpg_city'),
        listing_details.get('mpg_highway'),
        listing_details.get('fuel_type'),
        listing_details.get('mileage'),
        listing_details.get('number_of_doors'),
        listing_details.get('engine'),
        listing_details.get('interior_color'),
        listing_details.get('transmission'),
        listing_details.get('cars_rating'),
        listing_details.get('exterior_color'),
        listing_details.get('city'),
        listing_details.get('state'),
        listing_details.get('zip_code'),
        advanced_details,
        listing_details.get('price'),
        listing_id
    )
    cursor.execute(sql, params)
    cached_conn.commit()
    cursor.close()


def save_model(listing_id, model):
    cursor = cached_conn.cursor()
    sql = """
    UPDATE car SET 
      model = %s
    WHERE listing_id = %s
    """
    params = (
        model,
        listing_id
    )
    cursor.execute(sql, params)
    cached_conn.commit()
    cursor.close()

def save_trim(listing_id, trim):
    cursor = cached_conn.cursor()
    sql = """
        UPDATE car SET 
          trim = %s
        WHERE listing_id = %s
        """
    params = (
        trim,
        listing_id
    )
    cursor.execute(sql, params)
    cached_conn.commit()
    cursor.close()


def get_listings_to_load(page_num):
    cursor = cached_conn.cursor()
    offset = (page_num - 1) * page_size
    cursor.execute("SELECT listing_id FROM car WHERE price IS NULL ORDER BY listing_id DESC OFFSET %s LIMIT %s", (offset, page_size))
    results = cursor.fetchall()
    cursor.close()
    return list(map(lambda row: row[0], results))


def get_listings_with_vins(page_num):
    cursor = cached_conn.cursor()
    offset = (page_num - 1) * page_size
    cursor.execute("SELECT listing_id, vin, model, trim FROM car WHERE vin IS NOT NULL ORDER BY listing_id DESC OFFSET %s LIMIT %s", (offset, page_size))
    results = cursor.fetchall()
    cursor.close()
    return list(map(lambda row: {'listing_id': row[0], 'vin': row[1], 'model': row[2], 'trim': row[3]}, results))


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
