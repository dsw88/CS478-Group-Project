#############################################
# This script was used to correct the model of vehicles after the fact from VIN data
#############################################

import db
import scraping

page_num = 619
total_entries = 0
while True:
    print(page_num)
    details = db.get_listings_with_vins(page_num)
    if len(details) == 0:  # Proceed until there are no more to load
        break

    for detail in details:
        total_entries += 1
        print("Loading details for listing {}".format(detail['listing_id']))
        car_attributes = scraping.get_attributes_from_vin(detail['vin'])

        if car_attributes.get('Model'):
            new_model = car_attributes['Model']
            print("  Old model: {} New Model: {}".format(detail['model'], new_model))
            db.save_model(detail['listing_id'], new_model)

        if car_attributes.get('Trim'):
            new_trim = car_attributes['Trim']
            print("  Old trim: {} New trim: {}".format(detail['trim'], new_trim))
            db.save_trim(detail['listing_id'], new_trim)

    page_num += 1

print("Total entries: {}".format(total_entries))