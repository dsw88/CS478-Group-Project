from jtke import dbg

def save_detail_links(listing_ids):
    print(listing_ids)


# Get 30 pages (3000 cars per day)
for page_num in range(1,2):
    listing_ids = load_listings_page(page_num)
    save_detail_links(listing_ids)