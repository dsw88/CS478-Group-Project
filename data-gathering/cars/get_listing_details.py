import db
import scraping

page_num = 1
while True:
    print(page_num)
    listing_ids = db.get_listings_to_load(page_num)
    if len(listing_ids) == 0: # Proceed until there are no more to load
        break

    for listing_id in listing_ids:
        print("Loading details for listing {}".format(listing_id))
        listing_details = scraping.load_listing_detail_page(listing_id)
        if listing_details:
            db.save_listing_details(listing_id, listing_details)

    page_num += 1
