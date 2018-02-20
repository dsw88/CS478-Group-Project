import psycopg2
import os

db_user = os.environ.get('CARS_DB_USER')
db_pass = os.environ.get('CARS_DB_PASSS')
if not db_user or not db_pass:
    raise RuntimeError('You must specify the CARS_DB_USER and CARS_DB_PASS environment variables')
cached_conn = psycopg2.connect("dbname=scraped_cars user={} password={}".format(db_user, db_pass))

def execute_query(sql, params):
    print(sql)