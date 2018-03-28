import db
import scraping

def save_detail_links(listing_ids):
    for listing_id in listing_ids:
       db.insert_listing_id(listing_id)


# Get 30 pages (approx 10000 cars per day)
for page_num in range(1,101):
    listing_ids = scraping.load_listings_page(page_num)
    save_detail_links(listing_ids)